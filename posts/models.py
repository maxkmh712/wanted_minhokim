from django.db import models

from core.models import TimeStamp
from users.models import User

class Post(models.Model):
  title = models.CharField(max_length=300)
  content = models.CharField(max_length=2000, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  class Meta:
    db_table = 'posts'