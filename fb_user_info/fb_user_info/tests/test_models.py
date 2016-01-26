# coding: utf-8
from django.test import TestCase

from factories import TokenFactory, UserFacebookInfoFactory


class TokenTest(TestCase):
    def setUp(self):
        self.token = TokenFactory()

    def test_01_unicode(self):
        "Token must be a unicode"
        self.assertEqual(unicode(self.token), u"{0}".format(self.token.token))


class UserFacebookInfoTest(TestCase):
    def setUp(self):
        self.user_facebook = UserFacebookInfoFactory()

    def test_01_unicode(self):
        "User Facebook Info must be a unicode"
        self.assertEqual(
            unicode(self.user_facebook), u"{0}".format(
                self.user_facebook.name))
