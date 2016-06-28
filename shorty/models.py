from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    shortid = models.CharField(max_length=10, primary_key=True)
    fullMobileUrl = models.CharField(max_length=2000)
    fullDesktopUrl = models.CharField(max_length=2000)
    fullTabletUrl = models.CharField(max_length=2000)
    desktopRedirectCount = models.PositiveIntegerField(default=0)
    mobileRedirectCount = models.PositiveIntegerField(default=0)
    tabletRedirectCount = models.PositiveIntegerField(default=0)
    dateCreated = models.DateTimeField(auto_now_add=True)
