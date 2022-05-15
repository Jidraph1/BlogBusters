import os 

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jidraph:6720@localhost/blogbusters'    
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jidraph:6720@localhost/blogbusters'
    SECRET_KEY = 'jibberishjibberish'
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production': ProdConfig
}

    