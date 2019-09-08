from django.contrib.auth.models import Permission, Group, User
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from river.models import State, Workflow, TransitionApprovalMeta

from base.models import Ticket


# noinspection DuplicatedCode
class Command(BaseCommand):
    help = 'Bootstrapping database with necessary items'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Ticket)
        add_ticket_permission = Permission.objects.get(codename="add_ticket", content_type=content_type)
        change_ticket_permission = Permission.objects.get(codename="change_ticket", content_type=content_type)
        delete_ticket_permission = Permission.objects.get(codename="delete_ticket", content_type=content_type)

        team_leader_group, _ = Group.objects.update_or_create(name="team_leaders")
        team_leader_group.permissions.set([add_ticket_permission, change_ticket_permission, delete_ticket_permission])
        developer_group, _ = Group.objects.update_or_create(name="developers")
        developer_group.permissions.set([change_ticket_permission])

        open_state, _ = State.objects.update_or_create(label="Open", slug="open")
        in_progress_state, _ = State.objects.update_or_create(label="In Progress", slug="in_progress")
        resolved_state, _ = State.objects.update_or_create(label="Resolved", slug="resolved")
        re_open_state, _ = State.objects.update_or_create(label="Re Open", slug="re_open")
        closed_state, _ = State.objects.update_or_create(label="Closed", slug="closed")

        workflow, _ = Workflow.objects.update_or_create(content_type=content_type, field_name="status", defaults={"initial_state": open_state})

        open_to_in_progress, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, source_state=open_state, destination_state=in_progress_state)
        open_to_in_progress.groups.set([developer_group])

        in_progress_to_resolved, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, source_state=in_progress_state, destination_state=resolved_state)
        in_progress_to_resolved.groups.set([developer_group])

        resolved_to_closed, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, source_state=resolved_state, destination_state=closed_state)
        resolved_to_closed.groups.set([team_leader_group])

        resolved_to_re_open, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, source_state=resolved_state, destination_state=re_open_state)
        resolved_to_re_open.groups.set([team_leader_group])

        re_open_to_in_progress, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, source_state=re_open_state, destination_state=in_progress_state)
        re_open_to_in_progress.groups.set([developer_group])

        root = User.objects.filter(username="root").first() or User.objects.create_superuser(username="root", password="q1w2e3r4")
        root.groups.set([team_leader_group, developer_group])

        team_leader_1 = User.objects.filter(username="team_leader_1").first() or User.objects.create_user(username="team_leader_1", password="q1w2e3r4")
        team_leader_1.groups.set([team_leader_group])

        developer_1 = User.objects.filter(username="developer_1").first() or User.objects.create_superuser(username="developer_1", password="q1w2e3r4", groups=[developer_group])
        developer_1.groups.set([developer_group])

        self.stdout.write(self.style.SUCCESS('Successfully bootstrapped the db '))
