# coding: utf-8

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
            facebook_id=u"78964533213",
            link=u"https://www.facebook.com/app_scoped_user_id/78964533213",
            name="Mary Swansom",
            gender=None,
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

    def test_02_filter_list_facebook_by_gender(self):
        "Filter List Users Facebook by gender"
        response = self.client.get(
            "/api/v1/fb-user/?token={0}&gender=male".format(self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_03_detail_facebook_user(self):
        "Detail a Facebook User"
        response = self.client.get("/api/v1/fb-user/{0}/?token={1}".format(
            self.user_facebook.facebook_id, self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_04_facebook_user_does_not_exist(self):
        "Facebook User does not exist"
        response = self.client.get(
            "/api/v1/fb-user/does-not-exist/?token={0}".format(
                self.token.token))
        self.assertEqual(response.status_code, 404)

    def test_05_get_facebook_user_and_save_in_database(self):
        "Get user facebook info and save in database"
        self.client.get(
            "/api/v1/fb-user/789897897/?token={0}".format(
                self.token.token))
        create_new_user_facebook = create_facebook_user_info.delay(
            "7878415652")
        self.assertTrue(create_new_user_facebook, "7878415652")

    def test_06_delete_user_facebook(self):
        "Delete User Facebook"
        response = self.client.delete("/api/v1/fb-user/{0}/?token={1}".format(
            self.new_user_facebook.facebook_id, self.token.token))
        self.assertEqual(response.status_code, 204)
