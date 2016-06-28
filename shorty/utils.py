from models import ShortUrl

def createShortURL(shortid, fullMobileUrl, fullDesktopUrl, fullTabletUrl):
    shortUrl = ShortUrl(shortid=shortid,fullMobileUrl=fullMobileUrl,
                 fullDesktopUrl=fullDesktopUrl, fullTabletUrl=fullTabletUrl)
    shortUrl.save()
    return shortUrl.shortid
