# coding: utf-8
import logging
import requests

from django.core.paginator import Paginator
from django.conf import settings

from restless.dj import DjangoResource
from restless.exceptions import NotFound, Unauthorized
from restless.preparers import FieldsPreparer
from restless.resources import skip_prepare

from models import Token, UserFacebookInfo
from tasks import create_facebook_user_info

logger = logging.getLogger('fb_user_info.fb_user_info.resources')


class BaseResource(DjangoResource):
    DEFAULT_PAGINATOR = 10

    dict_filters = {}

    preparer = FieldsPreparer(fields={})

    def filters(self, request):
        items = {}
        for key, value in self.request.GET.items():
            if key in self.dict_filters:
                items[self.dict_filters.get(key)] = value
        return items

    def is_authenticated(self):
        try:
            self.token = Token.objects.get(token=self.request.GET.get('token'))
            return True
        except Token.DoesNotExist:
            raise Unauthorized(
                msg="Token {0} unauthorized or inexistent".format(
                    self.request.GET.get('token')))

    def serialize_list(self, data):
        data = self.paginate(data)
        self.meta = data.get('meta')
        return super(BaseResource, self).serialize_list(data.get('objects'))

    def wrap_list_response(self, data):
        return {
            'meta': self.meta,
            'objects': data,
        }

    def paginate(self, queryset):
        data = dict()

        limit = int(self.request.GET.get('limit', self.DEFAULT_PAGINATOR))
        self.paginator = Paginator(queryset, limit)
        self.page = int(self.request.GET.get('page', 1))

        meta = {
            'limit': limit,
            'next': self.paginator.page(self.page).has_next(),
            'previous': self.paginator.page(self.page).has_previous(),
            'total_count': self.paginator.count,
            'page': self.page,
        }

        data['meta'] = meta
        data['objects'] = self.paginator.page(self.page).object_list
        return data

    def get_graph_facebook_info(self, facebook_id):
        try:
            response = requests.get(
                'https://graph.facebook.com/' + str(facebook_id) +
                '?access_token={0}'.format(
                    settings.FACEBOOK_TOKEN), timeout=5).json()
            print response
            return self.prepare_graph_info(response).value
        except:
            return False

    @skip_prepare
    def prepare_graph_info(self, graph_info):
        if not graph_info['gender']:
            get_first_name = graph_info['name'].split('')[0]
            get_gender = requests.get(
                'https://api.genderize.io/?name={0}'.format(get_first_name))
        else:
            get_gender = graph_info['gender']
        graph_data = {
            'facebook_id': graph_info['id'],
            # 'username': graph_info['username'],
            'name': graph_info['name'],
            'gender': get_gender,
        }
        return False
        create_facebook_user_info.delay(graph_data)
        return graph_data


class UserFacebookInfoResource(BaseResource):
    fields = {
        'facebook_id': 'facebook_id',
        # 'username': 'username',
        'name': 'name',
        'gender': 'gender',
    }

    dict_filters = {
        'gender': 'gender',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = UserFacebookInfo.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.fields
        try:
            return self.queryset(request=self.request).get(facebook_id=pk)
        except:
            user_fb_info = self.get_graph_facebook_info(facebook_id=pk)
            user_fb_task = create_facebook_user_info.delay(user_fb_info)
            return self.queryset(request=self.request).get(
                facebook_id=user_fb_task.get('user_facebook.facebook_id'))

    def delete(self, pk):
        return UserFacebookInfo.objects.get(facebook_id=pk).delete()
