import urllib.request,json
from .models import Source,Article

#Getting apiKey

api_key = None

#Getting the news base url
base_url = None
article_base_url = None

def configure_request(app):
    global api_key,base_url,article_base_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]
    article_base_url = app.config["ARTICLE_API_BASE_URL"]

def get_sources(source):
    """
    Function that gets the json response to our url request
    """
    get_sources_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results= None

        if get_sources_response["sources"]:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    """
    Function that processes the source result and transform them into a list of objects
    Args:
    source_list: A list of dictionaries that contain movie details
    Returns:
    source_results: A list of Source objects
    """
    source_results=[]
    for source_item in source_list:
        id = source_item.get("id")
        name = source_item.get("name")
        description = source_item.get("description")
        url = source_item.get("url")
        category = source_item.get("category")


        source_object=Source(id,name,description,url,category)
        source_results.append(source_object)

        # print(source_list)

    return source_results

def get_news(id):
    '''Function thet gets the json response to our url request'''
    get_news_url = news_base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['news']:
            news_results_list = get_news_response['news']
            news_results = process_news(news_results_list)

    return news_results

def process_news(news_list):
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urlToImage:
            news_object = Article(id,title,description,url,urlToImage,publishedAt,content)
            news_results.append(article_object)

    return article_results
