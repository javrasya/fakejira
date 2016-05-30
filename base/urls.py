from django.conf.urls import url

from base.views import proceed_ticket

urlpatterns = [
    url(r'^proceed_ticket/(?P<ticket_id>\d+)/(?P<next_state_id>\d+)/$', proceed_ticket, name='proceed_ticket'),
]
