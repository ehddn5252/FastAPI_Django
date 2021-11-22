import pymysql
from ..project import settings

class DML:

    def __init__(self):
        db_instance = pymysql.connect(host=settings.DATABASES["default"]["HOST"],
                                      user=settings.DATABASES["default"]["USER"],
                                      password=settings.DATABASES["default"]["PASSWORD"],
                                      port=settings.DATABASES["default"]["PORT"],
                                      database=settings.DATABASES["default"]["HOST"],
                                      autocommit=settings.DATABASES['default']["AUTOCOMMIT"]
                                      )
