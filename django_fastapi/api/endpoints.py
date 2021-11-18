from typing import List

from fastapi import APIRouter
from django.http import HttpResponse
from api import models, schemas


api_router = APIRouter()


@api_router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate):
    item = models.Item.objects.create(**item.dict())
    return item

@api_router.get("/items", response_model=List[schemas.Item])
def read_items():
    items = list(models.Item.objects.all())
    return items

@api_router.post("/userinfos",response_model = List[schemas.UserInfo])
def create_user_info(user_info: schemas.UserInfoCreate):
    user_info = list(models.UserInfo.create(**user_info.dict()))
    return user_info

@api_router.get("/userinfos",response_model = List[schemas.UserInfo])
def read_user_info():
    user_infos = list(models.UserInfo.objects.all())
    return user_infos

