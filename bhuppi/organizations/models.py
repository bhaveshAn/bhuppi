from django.db import models
from accounts.models import User
import json

class Organization(models.Model):
    name = models.CharField(max_length=50, null=False)
    super_admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organization', default=None, blank=True, null=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_admin': self.super_admin.username if self.super_admin else None
        }
