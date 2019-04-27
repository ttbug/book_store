from app.net.http import Http
from flask import current_app


class BookStore():
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, key, page=1):
        url = cls.keyword_url.format(key, current_app.config['NUM_PER_PAGE'], cls.calculate_start(page))
        result = Http.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page-1)*current_app.config['NUM_PER_PAGE']
