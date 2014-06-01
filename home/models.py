from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
    user = models.ForeignKey(User)
    fb_id = models.BigIntegerField(null=True)
    photo = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)

