# coding: utf-8
import logging

from settings import celery_app

from models import UserFacebookInfo

logger = logging.getLogger('fb_user_info.fb_user_info.tasks')


@celery_app.task
def create_facebook_user_info(graph_info):
    logger.info(
        u"Start creation of User ID {0}".format(graph_info['facebook_id']))
    user_facebook, created = UserFacebookInfo.objects.get_or_create(
        facebook_id=graph_info['facebook_id'],
        # username=graph_info['username'],
        name=graph_info['name'],
        gender=graph_info['gender'],
    )
    logger.info(
        u"User ID {0} created with success".format(graph_info['facebook_id']))
