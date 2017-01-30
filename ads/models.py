from django.db import models

class Ads(models.Model):
    sku = models.CharField
    title = models.CharField(max_length=512, )
    category = models.CharField(max_length=512)
    description = models.TextField
    price = models.DecimalField
    stock = models.DecimalField
    photo1 = models.URLField(max_length=512, null=True)
    photo2 = models.URLField(max_length=512, null=True)
    photo3 = models.URLField(max_length=512, null=True)
    photo4 = models.URLField(max_length=512, null=True)
    photo5 = models.URLField(max_length=512, null=True)
    photo6 = models.URLField(max_length=512, null=True)
    youtube = models.CharField(max_length=512, null=True)
    type = models.CharField
    free_ship = models.BooleanField
    permalink = models.URLField(null=True)
    error = models.CharField(max_length=512, null=True)
    json_send = models.TextField(null=True)