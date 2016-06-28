1) "activate your virtualenv"
2) pip install -r requirements.txt
3) python manage.py test
4) python manage.py runserver

Create a shortURL & test it
- Install Chrome App Advanced REST Client (https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?utm_source=chrome-app-launcher-info-dialog)

- Launch ARC
URL: http://127.0.0.1:8000/shortenurl/
Method: POST
application/json
Raw heaers: Content-Type: application/json
Raw payload: {"mobile": "http://m.google.com", "tablet":"http://t.google.com", "desktop":"http://www.google.com"}

Click Send

The shortURL is in the bottom pane, make a note of that URL

http://127.0.0.1:8000/[shorturl from above]

Using Chrome Dev Tools, change your user agent to mobile & hit the url above again.
Now change your user agent to a tablet UA and try 1 more time.

Get all the urls
http://127.0.0.1:8000/geturls
