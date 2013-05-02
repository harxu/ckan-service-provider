DEBUG = False
TESTING = False
SECRET_KEY = 'please_replace_me'
USERNAME = 'admin'
PASSWORD = 'pass'

# database

SQLALCHEMY_DATABASE_URI = 'sqlite://'
SQLALCHEMY_ECHO = False

# webserver host and port

HOST = '0.0.0.0'
PORT = 8000

# logging

FROM_EMAIL = 'server-error@example.com'
ADMINS = ['yourname@example.com']  # where to send emails

LOG_FILE = '/tmp/ckan_service.log'

# project configuration
NAME = 'service'
