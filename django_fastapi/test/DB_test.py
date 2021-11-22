DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'd_f2',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

"""
self.connection: pymysql.connections.Connection = pymysql.connect(host= DATABASES['default']['HOST'],
                                                                  user=  DATABASES['default']['USER'],
                                                                  password=DATABASES['default']["PASSWORD"],
                                                                  port=DATABASES['default']["PORT"],
                                                                  autocommit=DATABASES['default']["AUTOCOMMIT"],
                                                                  database=DATABASES['default']["NAME"] ,
                                                                  #read_timeout=30 ,
                                                                  #connect_timeout=30 ,
                                                                  #cursorclass=pymysql.cursors.DictCursor)
                                                                  #charset=Info.DB.DBInstance2_CONNECTION_INFO["CHARSET"] ,
"""

