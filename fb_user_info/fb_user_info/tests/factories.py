# coding: utf-8
import factory
import uuid

from datetime import datetime

from django.contrib.auth.models import User

from fb_user_info.models import Token, UserFacebookInfo


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: u"user%s" % n)
    first_name = factory.Sequence(lambda n: u"User %s" % n)
    last_name = factory.Sequence(lambda n: u"Final Name %s" % n)


class TokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token

    user = factory.SubFactory(UserFactory)
    token = uuid.uuid4()
    date_added = datetime.now()
    is_active = True


class UserFacebookInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserFacebookInfo

    facebook_id = factory.Sequence(lambda n: u"132060404%s" % n)
    link = u"https://www.facebook.com/app_scoped_user_id/{0}".format(
        facebook_id)
    name = factory.Sequence(lambda n: u"User Random%s" % n)
    gender = 'male'
