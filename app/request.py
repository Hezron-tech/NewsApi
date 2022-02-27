from app import app
import urllib.request,json
from .models import news



News = news.News

api_key=None
source_url=None

# Getting api key
api_key ='dc38d2088e954eb6a28aa1c12dce28e7'
# Getting base url
# base_url='https://newsapi.org/v2/top-headlines/sources?category={}?&apiKey={}'
# Getting the  base url
base_url = app.config["NEWS_ARTICLE_URL"]


def get_news(title):
    get_news_url =base_url.format(title,api_key)
    


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
        title=new.get('title')
        urlToImage=new.get('urlToImage')
        description=new.get('description')
        url=new.get('url')
        publishedAt=new.get('publishedAt')
        # country=new.get('country')

        
        news_object=News(id,title,urlToImage,description,url,publishedAt)

        news_results.append(news_object)

    return news_results    