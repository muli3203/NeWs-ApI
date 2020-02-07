
import urllib.request,json
from .models import News, Articles


api_key = None
base_url = None
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config["NEWS_SOURCES_BASE_URL"]
    articles_url = app.config["ARTICLES_BASE_URL"]

def process_sources(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news objects

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        print(news_item)
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if description:
            news_object = News(id,name,description,url,category,language,country)
            news_results.append(news_object)


    return news_results
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_sources(news_results_list)

    return news_results

def process_articles(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news objects

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        author =  news_item.get('author')
        title =  news_item.get('title')
        description =  news_item.get('description')
        url =  news_item.get('url')
        urlToImage =  news_item.get('urlToImage')
        publishedAt =  news_item.get('publishedAt')
        content =  news_item.get('content')

        if description:
            news_object = Articles(id,author, title, description, url, urlToImage, publishedAt, content)
            news_results.append(news_object)

    return news_results

def get_news_articles(news_id):
    get_news_articles_url = articles_url.format(news_id,api_key)

    with urllib.request.urlopen(get_news_articles_url) as url:
        news_articles_data = url.read()
        news_articles_response = json.loads(news_articles_data)


        if news_articles_response['articles']:
            articles_results= news_articles_response['articles']
            articles = process_articles(articles_results)

    return articles