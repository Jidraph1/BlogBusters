import os 

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jidraph:6720@localhost/blogbusters'    
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):

    # SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL').replace("://", "ql://",1)
    DEBUG = True

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jidraph:6720@localhost/blogbusters'
    SECRET_KEY = 'jibberishjibberish'


config_options = {
    'development' : DevConfig,
    'production': ProdConfig
}

    