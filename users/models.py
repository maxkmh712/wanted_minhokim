from django.db import models

from core.models import TimeStamp

class User(TimeStamp):
  name = models.CharField(max_length=100, null=True)
  email = models.CharField(max_length=200, unique=True)
  password = models.CharField(max_length=200)

  class Meta:
    db_table = 'users'