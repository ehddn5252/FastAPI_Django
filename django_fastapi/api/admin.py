from django.contrib import admin

from .models import Item
from .models import UserInfo
#from .models import Test


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_password")

"""
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("test_id","test_password")
"""
