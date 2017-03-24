# coding=utf-8

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:    
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(40)

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True

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
    FLASKY_SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    HOST = '0.0.0.0'
    POST = 8899
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql://www-data:www-data@localhost/flasky'


class TestingConfig(Config):
    SERVER_NAME = 'localhost'
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'mysql://www-data:www-data@localhost/test'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://www-data:www-data@localhost/flasky'

    @staticmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from logging.handlers import SMTPHandler 
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost = (cls.MAIL_SERVER,cls.MAIL_PORT),
            fromaddr = cls.FLASKY_MAIL_SENDER,
            toaddr   = cls.FLASKY_ADMIN,
            subject  = cls.FLASKY_MAIL_SUBJECT_PREFIX + 'Application Error',
            credentials = credentials,
            secure   = secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

        from logging.handlers import SysLogHandler 
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
