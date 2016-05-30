from django.contrib import admin

# Register your models here.
from django.core.urlresolvers import reverse

from base.models import Ticket


def create_river_button(obj, proceeding):
    return """
        <input
            type="button"
            style="margin:2px;2px;2px;2px;"
            value="%s"
            onclick = "location.href=\'%s\'"
        />
    """ % (proceeding.meta.transition,
           reverse('proceed_ticket',
                   kwargs={'ticket_id': obj.pk, 'next_state_id': proceeding.meta.transition.destination_state.pk})
           )


class TicketAdmin(admin.ModelAdmin):
    list_display = ('no', 'subject', 'description', 'status', 'river_actions')

    def get_list_display(self, request):
        self.user = request.user
        return super(TicketAdmin, self).get_list_display(request)

    def river_actions(self, obj):
        content = ""
        for proceeding in obj.get_available_proceedings(self.user):
            content += create_river_button(obj, proceeding)

        return content

    river_actions.allow_tags = True


admin.site.register(Ticket, TicketAdmin)
