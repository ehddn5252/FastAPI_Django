from django.contrib import admin

from .models import Item
from .models import UserInfo
from .models import Login

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_password")

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_password")
