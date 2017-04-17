from django.db import models
from django.contrib.auth.models import User
from vendors.meli.meli import Meli
from django.conf import settings
import time

class MeliAccount(models.Model):
    userid = models.CharField(max_length=256)
    nickname = models.CharField(max_length=256)
    refresh_token = models.CharField(max_length=512)
    expires = models.BigIntegerField()
    owner = models.ForeignKey(User, related_name='meli_accounts')
    access_token = models.CharField(max_length=512)
    
    def verify_refresh_token(self):
        if time.time() >= self.expires:
            meli = Meli(client_id=settings.MELI_CLIENT_ID, client_secret=settings.MELI_CLIENTE_SECRET, access_token=self.access_token)
            self.refresh_token = meli.get_refresh_token()
            
    def __str__(self):
        return self.nickname
            
class CopyAccount(models.Model):
    STATUS_CHOICES = (('pending', 'Pendente'), ('running','Copiando'), ('done', 'Concluído'))
    copy_from = models.ForeignKey(MeliAccount, related_name='copied_from')
    copy_to = models.ForeignKey(MeliAccount, related_name='copied_to')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')