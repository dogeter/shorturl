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
    urls = list(ShortUrl.objects.all())
    print urls[0].url_age

    """
    for url in urls:
        url.fields.append("urlAge: %s" % url.url_age)
    """
    return HttpResponse(serializers.serialize('json', urls))


{
"model": "shorty.shorturl", "pk": "138CA2", "fields":

    {"fullMobileUrl": "m.foo.com", "fullDesktopUrl": "d.foo.com",
    "fullTabletUrl": "t.foo.com", "desktopRedirectCount": 2,
    "mobileRedirectCount": 0, "tabletRedirectCount": 0,
    "dateCreated": "2016-06-28T05:09:50.767Z"}
}
