from django.contrib import admin

from .models import Item, Login
from .models import UserInfo
from .models import Test1

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_password")

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ("user_id", "user_password")

@admin.register(Test1)
class Test1Admin(admin.ModelAdmin):
    list_display = ("test1", "test2")
