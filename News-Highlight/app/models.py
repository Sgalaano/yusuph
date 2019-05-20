class Source:
    """
    Source class to define News Sources
    """
    def __init__(self,id,name,description,url,category):
        self.id= id
        self.name = name
        self.description = description
        self.url= url
        self.category = category

class news:
    """
    news class to define Source News
    """
    def __init__(self,id,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content