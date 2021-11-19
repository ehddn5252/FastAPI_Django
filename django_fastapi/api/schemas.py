from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True


# 2021.11.17 added
class UserInfoBase(BaseModel):
    user_id: str
    user_password: str = None

class UserInfoCreate(UserInfoBase):
    pass

class UserInfo(UserInfoBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True


class LoginBase(BaseModel):
    user_id: str
    user_password: str = None

class LoginCreate(BaseModel):
    pass

class Login(LoginBase):
    id: int
    owner_id: int

