from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    shortid = models.CharField(max_length=6)
    fullMobileUrl = models.CharField(max_length=500)
    fullDesktopUrl = models.CharField(max_length=500)
