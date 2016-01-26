# coding: utf-8
import json

from datetime import datetime
from decimal import Decimal

from django.test import TestCase

from fb_user_info.tasks import create_facebook_user_info

from factories import TokenFactory, UserFacebookInfoFactory


def jdefault(o):
    if type(o) is datetime.date or type(o) is datetime:
        return o.isoformat()
    if type(o) is Decimal:
        return str(o)
    return o.__dict__


class BaseResourceTest(TestCase):
    def setUp(self):
        self.token = TokenFactory()
        self.user_facebook = UserFacebookInfoFactory()

        self.new_user_facebook = UserFacebookInfoFactory.create(
            facebook_id=u"987465416",
            username=u"new-user",
            name="New User",
            gender="female",
        )

    def test_01_unauthorized(self):
        "Request without token does not pass"
        response = self.client.get("/api/v1/fb-user/")
        self.assertEqual(response.status_code, 401)


class UserFacebookInfoResourceTest(BaseResourceTest):
    def test_01_list_facebook_users(self):
        "List all Facebook Users"
        response = self.client.get("/api/v1/fb-user/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_02_detail_facebook_user(self):
        "Detail a Facebook User"
        response = self.client.get("/api/v1/fb-user/{0}/?token={1}".format(
            self.user_facebook.facebook_id, self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_03_facebook_user_does_not_exist(self):
        "Facebook User does not exist"
        response = self.client.get("/api/v1/fb-user/000000/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 404)

    def test_04_create_type(self):
        "Create a type"
        response = self.client.post("/api/v1/fb-user/?token={0}".format(
            self.token.token), json.dumps(
            self.new_user_facebook.facebook_id, default=jdefault),
            content_type="application/json")

        create_new_user_facebook = create_facebook_user_info.delay(
            self.new_user_facebook)
        self.assertTrue(create_new_user_facebook, "987465416")
        self.assertEqual(response.status_code, 201)

    def test_05_delete_type(self):
        "Delete a type"
        response = self.client.delete("/api/v1/fb-user/{0}/?token={1}".format(
            self.new_user_facebook.facebook_id, self.token.token))
        self.assertEqual(response.status_code, 204)