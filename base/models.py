from __future__ import unicode_literals

import uuid

from django.db import models

# Create your models here.
from river.models.fields.state import StateField


class Ticket(models.Model):
    no = models.CharField("Ticket Number", max_length=50, default=uuid.uuid4, null=False, blank=False, editable=False,
                          unique=True)
    subject = models.CharField("Subject", max_length=100, null=False, blank=False)
    description = models.TextField("Description", max_length=500, null=True, blank=True)

    status = StateField(editable=False)

    def natural_key(self):
        return self.no

