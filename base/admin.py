import river_admin
from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe

from base.models import Ticket


def create_river_button(obj, transition_approval):
    approve_ticket_url = reverse('approve_ticket', kwargs={'ticket_id': obj.pk, 'next_state_id': transition_approval.transition.destination_state.pk})
    return f"""
        <input
            type="button"
            style="margin:2px;2px;2px;2px;"
            value="{transition_approval.transition.source_state} -> {transition_approval.transition.destination_state}"
            onclick="location.href=\'{approve_ticket_url}\'"
        />
    """


class TicketAdmin(admin.ModelAdmin):
    list_display = ('no', 'subject', 'description', 'status', 'river_actions')

    def get_list_display(self, request):
        self.user = request.user
        return super(TicketAdmin, self).get_list_display(request)

    def river_actions(self, obj):
        content = ""
        for transition_approval in obj.river.status.get_available_approvals(as_user=self.user):
            content += create_river_button(obj, transition_approval)

        return mark_safe(content)


admin.site.register(Ticket, TicketAdmin)


class TicketRiverAdmin(river_admin.RiverAdmin):
    name = "Issue Tracking Flow"
    icon = "mdi-ticket-account"
    list_displays = ['pk', 'no', 'subject', 'description', 'status']


river_admin.site.register(Ticket, "status", TicketRiverAdmin)
