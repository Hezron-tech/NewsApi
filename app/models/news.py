class News:


    def __init__(self,id,title,urlToImage,description,url,publishedAt):
        self.id=id
        self.title=title
        self.urlToImage=urlToImage
        self.description=description
        self.url=url
        # self.category=category
        self.publishedAt=publishedAt
        

# class Article:
#     '''
#     Class that instantiates objects of the news article objects of the news sources
#     '''
#     def __init__(self,author,description,time,url,image,title):
#         self.author = author
#         self.description = description
#         self.time = time
#         self.url = url
#         self.image = image
#         self.title = title

# class Category:
#     '''
#     Class that instantiates objects of the news categories objects of the news sources
#     '''
#     def __init__(self,author,description,time,url,image,title):
#         self.author = author
#         self.description = description
#         self.time = time
#         self.url = url
#         self.image = image
#         self.title = title