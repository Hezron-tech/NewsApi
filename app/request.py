from app import app
import urllib.request,json
from .models import news,Article,category



News = news.News

api_key=None
source_url=None

# Getting api key
api_key ='dc38d2088e954eb6a28aa1c12dce28e7'
# Getting base url
# base_url='https://newsapi.org/v2/top-headlines/sources?category={}?&apiKey={}'
# Getting the  base url
base_url = app.config["NEWS_SOURCE_URL"]


def get_news(category):
    get_news_url =base_url.format(category,api_key)
    


    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)
        news_results=None


        if get_news_response ["sources"]:
            new_results_list=get_news_response["sources"]
            news_results=process_results(new_results_list)


    return news_results
def process_results(news_list):
    news_results=[]

    for new in news_list:
        id=new.get('id')
        name=new.get('name')
        description=new.get('description')
        url=new.get('url')
        category=new.get('category')
        country=new.get('country')

        
        news_object=News(id,name,description,url,category,country)

        news_results.append(news_object)

    return news_results  
    
def article_source(id):
    article_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(article_source_url)
    with urllib.request.urlopen(article_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_results = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_results = process_articles_results(article_source_list)


    return article_source_results

def process_articles_results(news):
    '''
    function that processes the json files of articles from the api key
    '''
    article_source_results = []
    for article in news:
        author = article.get('author')
        description = article.get('description')
        time = article.get('publishedAt')
        url = article.get('urlToImage')
        image = article.get('url')
        title = article.get ('title')

        if url:
            article_objects = Article(author,description,time,image,url,title)
            article_source_results.append(article_objects)

    return article_source_results      