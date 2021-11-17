from django.contrib import admin

from api.models import Item
from api.models import UserInfo


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "password")
    