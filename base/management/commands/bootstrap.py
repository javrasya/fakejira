from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from river.models import State, Workflow, TransitionApprovalMeta, TransitionMeta

from base.models import Ticket


# noinspection DuplicatedCode
class Command(BaseCommand):
    help = 'Bootstrapping database with necessary items'

    @transaction.atomic()
    def handle(self, *args, **options):
        workflow_content_type = ContentType.objects.get_for_model(Workflow)
        content_type = ContentType.objects.get_for_model(Ticket)

        add_ticket_permission = Permission.objects.get(codename="add_ticket", content_type=content_type)
        change_ticket_permission = Permission.objects.get(codename="change_ticket", content_type=content_type)
        delete_ticket_permission = Permission.objects.get(codename="delete_ticket", content_type=content_type)

        view_workflow_permission = Permission.objects.get(codename="view_workflow", content_type=workflow_content_type)

        team_leader_group, _ = Group.objects.update_or_create(name="team_leaders")
        team_leader_group.permissions.set([add_ticket_permission, change_ticket_permission, delete_ticket_permission, view_workflow_permission])
        developer_group, _ = Group.objects.update_or_create(name="developers")
        developer_group.permissions.set([change_ticket_permission, view_workflow_permission])

        open_state, _ = State.objects.update_or_create(label="Open", slug="open")
        in_progress_state, _ = State.objects.update_or_create(label="In Progress", slug="in_progress")
        resolved_state, _ = State.objects.update_or_create(label="Resolved", slug="resolved")
        re_open_state, _ = State.objects.update_or_create(label="Re Open", slug="re_open")
        closed_state, _ = State.objects.update_or_create(label="Closed", slug="closed")

        workflow, _ = Workflow.objects.update_or_create(content_type=content_type, field_name="status", defaults={"initial_state": open_state})

        open_to_in_progress, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=open_state, destination_state=in_progress_state)
        in_progress_to_resolved, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=in_progress_state, destination_state=resolved_state)
        resolved_to_closed, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=resolved_state, destination_state=closed_state)
        resolved_to_re_open, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=resolved_state, destination_state=re_open_state)
        re_open_to_in_progress, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=re_open_state, destination_state=in_progress_state)

        open_to_in_progress_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=open_to_in_progress)
        open_to_in_progress_meta.groups.set([developer_group])

        in_progress_to_resolved_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=in_progress_to_resolved)
        in_progress_to_resolved_meta.groups.set([developer_group])

        resolved_to_closed_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=resolved_to_closed)
        resolved_to_closed_meta.groups.set([team_leader_group])

        resolved_to_re_open_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=resolved_to_re_open)
        resolved_to_re_open_meta.groups.set([team_leader_group])

        re_open_to_in_progress_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=re_open_to_in_progress)
        re_open_to_in_progress_meta.groups.set([developer_group])

        root = User.objects.filter(username="root").first() or User.objects.create_superuser("root", "", "q1w2e3r4")
        root.groups.set([team_leader_group, developer_group])

        team_leader_1 = User.objects.filter(username="team_leader_1").first() or User.objects.create_user("team_leader_1", password="q1w2e3r4", is_staff=True)
        team_leader_1.groups.set([team_leader_group])

        developer_1 = User.objects.filter(username="developer_1").first() or User.objects.create_user("developer_1", password="q1w2e3r4", is_staff=True)
        developer_1.groups.set([developer_group])

        self.stdout.write(self.style.SUCCESS('Successfully bootstrapped the db '))
