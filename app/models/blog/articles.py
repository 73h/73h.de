from models.blog.article import Article


class Articles:

    def __init__(self, articles: list):
        self.articles = list()
        for article in articles:
            self.articles.append(Article(**article))
