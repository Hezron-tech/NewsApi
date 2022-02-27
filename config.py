
class Config:
    '''
    General configuration parent class
    '''
    NEWS_BASE_URL='https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    NEWS_SOURCE_URL='https://newsapi.org/v2/top-headlines/sources?language=en&category={}&apiKey={}'
    NEWS_TOP_HEADLINES_URL='https://newsapi.org/v2/top-headlines?country={}'

    pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

