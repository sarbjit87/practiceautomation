import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') #secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    FILE_UPLOAD = os.path.join(basedir, 'uploads')
    APP_NAME = "Practice Automation"
    #LDAP_LOGIN_ENABLED = True
    #LDAP_PROVIDER_URL = 'ldap://ldap.forumsys.com:389/'
    #LDAP_PROTOCOL_VERSION = 3
