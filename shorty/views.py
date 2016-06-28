from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from models import ShortUrl
from django.core import serializers
from user_agents import parse
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.test import TestCase
import json
import utils
import uuid

@csrf_exempt
def shortenURL(request):
    if request.method == 'POST':
        try:
            urls = json.loads(request.body)
        except:
            print "invalid request"

        success = False
        while not success:
            #create random shortURL
            #It's possible, but unlikely, this isn't unique
            shortURL = uuid.uuid4().hex[:10].upper()
                       
            try:
                savedShortUrl = utils.createShortURL(shortURL, urls["mobile"], urls["desktop"], urls["tablet"])
                success = True
            except:
                print "found potential duplicate"

        return HttpResponse(savedShortUrl)

def redirect(request, shorturl):
    #send a 500 error shortURL doesn't exist
    try:
        urlObject = ShortUrl.objects.get(shortid=shorturl)
    except:
        return HttpResponseServerError()

    #check UA of request
    #user_agents is awesome! (pip install pyyaml ua-parser user-agents)
    userAgent = parse(request.META.get('HTTP_USER_AGENT', ''))

    if urlObject:
        if userAgent.is_mobile:
            urlObject.mobileRedirectCount += 1
            urlObject.save()
            return HttpResponseRedirect(urlObject.fullMobileUrl)

        elif userAgent.is_tablet:
            urlObject.tabletRedirectCount += 1
            urlObject.save()
            return HttpResponseRedirect(urlObject.fullTabletUrl)

        elif userAgent.is_pc:
            urlObject.desktopRedirectCount += 1
            urlObject.save()
            return HttpResponseRedirect(urlObject.fullDesktopUrl)

            #debug
            #return HttpResponse(serializers.serialize('json', [urlObject]))
def getUrls(request):
    urls = ShortUrl.objects.all()
    #for shorturl in urls:


    return HttpResponse(serializers.serialize('json', urls))
