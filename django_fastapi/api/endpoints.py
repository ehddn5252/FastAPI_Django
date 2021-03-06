from typing import List

from fastapi import APIRouter
from django.http import HttpResponse
from api import models, schemas
from fastapi import FastAPI, Request
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from random import *
import json
import jwt

api_router = APIRouter()
app = FastAPI()

@api_router.get("/")
def abc():
    return {"message": "hello"}

@api_router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate):
    # 객체 생성
    item = models.Item.objects.create(**item.dict())
    return item

@api_router.get("/items", response_model=List[schemas.Item])
def read_items():
    # 객체 가져온다.
    items = list(models.Item.objects.all())
    return items

@api_router.post("/userinfos",response_model = List[schemas.UserInfo])
def create_user_info(user_info: schemas.UserInfoCreate, request: Request):
    client_host = request.client.host
    exist_flag = False
    user_infos = list(models.UserInfo.objects.all())
    for exist_user_info in user_infos:
        if model_to_dict(exist_user_info) == user_info:
            exist_flag = True
    if not exist_flag:
        created_user_info = list(models.UserInfo.create(**user_info.dict()))
        return created_user_info
    return HttpResponse("user_id is already existed please try other id")

@api_router.get("/userinfos", response_model=List[schemas.UserInfo])
def read_user_info():
    user_infos = list(models.UserInfo.objects.all())
    return user_infos

@api_router.post("/login")
def create_login(login):
    login = list(models.Login.create(**login.dict()))
    return login

@api_router.get("/login")
def read_login():
    login = list(models.Login.objects.all())
    return login

@api_router.get("/test1/{test1}")
def create_test1(test1):
    #test = list(models.Test1.objects.create(**test1.dict()))
    dict = {"test1": test1}
    test1 = list(models.Test1.objects.create())
    print("====================")
    print(test1)
    test1[0] = {"test1": "test1", "test2": "test2", "token": "token"}
    return test1

@api_router.get("/test1")
def read_test1():
    import base64
    tests = list(models.Test1.objects.all())
    # JWT 는 대칭키 방식을 사용하며 encode 와 decode 할 때 같은 key 를 사용 해야한다
    secret_key = "secret_key"
    algorithm = "HS256"

    for index, test in enumerate(tests):
        encoded_jwt = jwt.encode(payload={"token": tests[index].token}, key=secret_key, algorithm=algorithm)
        tests[index].token = encoded_jwt
    print(type(tests[0].test1))
    #decoded_jwt = jwt.decode(jwt=encoded_jwt, key=secret_key, algorithms=algorithm)
    return tests
