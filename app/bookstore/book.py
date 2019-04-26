from app.net.http import Http


class BookStore():
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, key, count=15, start=0):
        url = cls.keyword_url.format(key, count, start)
        result = Http.get(url)
        return result
