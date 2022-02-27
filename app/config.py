
class Config:
    '''
    General configuration parent class
    '''
    NEWS_BASE_URL='https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    NEWS_ARTICLE_URL='https://newsapi.org/v2/sources?language=en&headlines={}&apiKey={}'
    # NEWS_SOURCE_URL='https://newsapi.org/v2/top-headlines/sources?language=en&category={}&apiKey={}'
    NEWS_TOP_HEADLINES_URL='https://newsapi.org/v2/top-headlines?country={}'

    pass
# 'https://newsapi.org/v2/everything?q=tesla&from=2022-01-27&sortBy=publishedAt&apiKey'
# https://newsapi.org/v2/sources?apiKey={}'
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

