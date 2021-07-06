from django.test import TestCase
from .models import Url
from .utils import create_random_string


class UrlModelTestCase(TestCase):
    def setUp(self):
        self.url = Url.objects.create(original_url='https://python.com/',
                                      shortened_url='https://url.sh/RaND0M')

    def test_url_str(self):
        self.assertEqual(self.url.__str__(),
                         f'{self.url.original_url} -> {self.url.shortened_url}')


class UrlEncodeAPITestCase(TestCase):
    def setUp(self):
        pass

    def test_bad_request(self):
        pass

    def test_encode_url(self):
        pass

    def test_url_exists(self):
        pass

    def test_random_string_exists(self):
        pass


class UrlDecodeAPITestCase(TestCase):
    def setUp(self):
        pass

    def test_decode_url(self):
        pass


class RandomStringTestCase(TestCase):
    def setUp(self):
        pass

    def test_decode_url(self):
        pass
