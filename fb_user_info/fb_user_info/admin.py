# coding: utf-8
from django.contrib import admin

from models import Token, UserFacebookInfo


class TokenAdmin(admin.ModelAdmin):
    list_display = ("token", "user", "date_added", "is_active",)
    list_filter = ("is_active",)
    date_hierarchy = "date_added"
    search_fields = ("user__username", "token",)


class UserFacebookInfoAdmin(admin.ModelAdmin):
    list_display = ("facebook_id", "link", "name", "gender", )
    list_filter = ("gender",)
    search_fields = ("name",)


admin.site.register(Token, TokenAdmin)
admin.site.register(
    UserFacebookInfo, UserFacebookInfoAdmin)
