from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str = None
    description2: str = None

class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# 2021.11.17 added
class UserInfoBase(BaseModel):
    id:str
    password: str = None

class UserInfoCreate(UserInfoBase):
    pass


class UserInfo(UserInfoBase):
    User_info_id: int

    class config:
        orm_mode = True
