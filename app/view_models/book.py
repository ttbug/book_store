class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.price = book['price']
        self.author = '，'.join(book['author']),
        self.pages = book['pages'] or '',
        self.summary = book['summary'] or '',
        self.image = book['image']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, book_store, keyword):
        self.total = book_store.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in book_store.books]


# 统一返回结果
class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        pass

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            returned['total'] = len(data['books'])
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]

        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'price': data['price'],
            'author': '，'.join(data['author']),
            'pages': data['pages'] or '',
            'summary': data['summary'] or '',
            'image': data['image']
        }

        return book
