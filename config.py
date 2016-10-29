# coding=utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(40)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <admin@windard.com>'
    FLASKY_ADMIN = os.environ.get('USERNAME')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    host = '0.0.0.0'
    port = 8899
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 597
    MAIL_USE_TLS = True
    MAIL_USERNAME = '1106911190@qq.com'
    MAIL_PASSWORD = 'XXXXXX'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URL = 'mysql://root:123456@localhost/flasky'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URL = 'mysql://root:123456@localhost/flasky'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = 'mysql://root:123456@localhost/flasky'

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
