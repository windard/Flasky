# coding=utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(40)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    # FLASKY_MAIL_SENDER = 'windard@outlook.com'
    FLASKY_MAIL_SENDER = '1106911190@qq.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGES = 30
    FLASKY_COMMENTS_PER_PAGE = 50

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    HOST = '0.0.0.0'
    POST = 8899
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql://www-data:www-data@localhost/flasky'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'mysql://www-data:www-data@localhost/flasky'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://www-data:www-data@localhost/flasky'

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
