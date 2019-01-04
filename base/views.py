from django.urls import reverse
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
from river.models import State

from base.models import Ticket


def approve_ticket(request, ticket_id, next_state_id=None):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    next_state = get_object_or_404(State, pk=next_state_id)

    try:
        ticket.river.status.approve(as_user=request.user, next_state=next_state)
        return redirect(reverse('admin:base_ticket_changelist'))
    except Exception as e:
        return HttpResponse(e.message)
