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


"""
# 2021.11.18 added
class TestBase(BaseModel):
    test_id: int
    test_password: str = None
    test_description: str = None

class TestCreate(TestBase):
    pass

class Test(TestBase):
    user_test_id: int
    class config:
        orm_mode = True
"""
