from django.db import models
from django.contrib.auth.models import User

class MeliAccount(models.Model):
    userid = models.CharField(max_length=256)
    nickname = models.CharField(max_length=256)
    refresh_token = models.CharField(max_length=512)
    expires = models.BigIntegerField
    owner = models.ForeignKey(User, related_name='meli_accounts')