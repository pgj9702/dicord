# mysql
import pymysql

# heroku db settings
from DB_SETTINGS import HEROKU_DB_SETTINGS

# url parser
import urlparse3
import sys
import os

# DB_conn
def getConnection():
    heroku_db_settings = HEROKU_DB_SETTINGS

    urlparse3.uses_netloc.append('mysql')

    try:
        # DB connect
        heroku_db = pymysql.connect(
            user=heroku_db_settings['user'],
            passwd=heroku_db_settings['passwd'],
            host=heroku_db_settings['host'],
            db=heroku_db_settings['db'],
            charset='utf8'
        )

    except Exception:
        print('Unexpected error:', sys.exc_info())



