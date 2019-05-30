import os
from dotenv import load_dotenv
load_dotenv()


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Configurations for development"""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for testing, with separate test database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB')
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production"""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
