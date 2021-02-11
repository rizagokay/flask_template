import os

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY='Vdcho0KS4qoKKRltWcgi6Q'
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "."
    USER_ID = "d788adc7-9bb0-4e10-88e7-6973f8cbd932"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APP_NAME = "Sample Flask App"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///%s' % os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'app.sqlite')
    DEBUG = True

class TestingConfig(Config):
    TESTING = True