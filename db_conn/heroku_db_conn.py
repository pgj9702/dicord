# mysql
import pymysql

# heroku db settings
from DB_SETTINGS import HEROKU_DB_SETTINGS

heroku_db_settings = HEROKU_DB_SETTINGS

# DB connect
heroku_db = pymysql.connect(
    user=heroku_db_settings['user'],
    passwd=heroku_db_settings['passwd'],
    host=heroku_db_settings['host'],
    db=heroku_db_settings['db'],
    charset='utf8'
)