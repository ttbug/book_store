'''
图书数据获取api，基地址：http://t.yushu.im
关键字搜索：http://t.yushu.im/v2/book/search?q={}&start={}&end={}
isbn搜索：http://t.yushu.im/v2/book/isbn/{isbn}
'''

from flask import jsonify, request
import json

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection
from . import web
from app.bookstore.book import BookStore
from app.tools.helper import is_isbn_or_key


@web.route('/book/search')
def search():
    '''
    :param q: 搜索关键字 or isbn
    :param page:
    :return:
    '''

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        book_store = BookStore()

        if isbn_or_key == 'isbn':
            book_store.search_by_isbn(q)
        else:
            book_store.search_by_keyword(q, page)

        books.fill(book_store, q)
        # 不能够序列化的类型使用default指定的函数进行序列化
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify({'msg': form.errors})
