from django.db import IntegrityError
from django.test import TestCase, RequestFactory
import views
import utils
import uuid
import json

class UnitTests(TestCase):
    def test_create_short_url(self):
        shortURL = uuid.uuid4().hex[:10].upper()
        shortUrlPostSave = utils.createShortURL(shortURL, 'm.google.com',
                                        'google.com', 't.google.com')
        self.assertEqual(shortUrlPostSave, shortURL)

    def test_dupe_short_url(self):
        shortURL = 'steven'
        with self.assertRaises(IntegrityError):
            shortUrlPostSave = utils.createShortURL(shortURL, 'm.google.com',
                                'google.com', 't.google.com')
            shortUrlPostSave = utils.createShortURL(shortURL, 'm.google.com',
                                'google.com', 't.google.com')

class IntegrationTests(TestCase):
    def test_shortenUrl(self):
        jsonArgs = {
            "mobile":"http://m.foo.com",
            "tablet":"http://t.foo.com",
            "desktop":"http://www.fark.com"
        }
        print json.dumps(jsonArgs)
        response = self.client.post("/shortenurl/",
                                    json.dumps(jsonArgs),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
