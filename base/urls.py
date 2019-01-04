from django.conf.urls import url

from base.views import approve_ticket

urlpatterns = [
    url(r'^approve_ticket/(?P<ticket_id>\d+)/(?P<next_state_id>\d+)/$', approve_ticket, name='approve_ticket'),
]
