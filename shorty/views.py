from django.http import HttpResponse
from django.shortcuts import render
from models import ShortUrl
from django.core import serializers

def create_internal(shortid, fullMobile, fullDesktop):
    s = ShortUrl(shortid=shortid,fullMobileUrl=fullMobile, fullDesktopUrl=fullDesktop)
    s.save()
    return s

# Create your views here.
def create(request):
    json = serializers.serialize('json', [create_internal('abc', 'http1', 'http2')])
    return HttpResponse(json)

def load(request, shorturl):
    print shorturl
    o = ShortUrl.objects.get(id=shorturl)
    return HttpResponse(serializers.serialize('json', [o]))
