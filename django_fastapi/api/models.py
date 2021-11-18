from django.db import models
from django.conf import settings

class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="items"
    )

# 여기는 보여지는 이름이다.
class UserInfo(models.Model):
    user_id = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="userinfos"
    )

# 여기는 보여지는 이름이다.
class Login(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    user_password = models.CharField(max_length=50)
    id2 = models.IntegerField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Login"
    )