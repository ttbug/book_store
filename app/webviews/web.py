'''
图书数据获取api，基地址：http://t.yushu.im
关键字搜索：http://t.yushu.im/v2/book/search?q={}&start={}&end={}
isbn搜索：http://t.yushu.im/v2/book/isbn/{isbn}
'''

from flask import jsonify, request

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

    q = request.args.get('q')
    page = request.args.get('page')

    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'key':
        result = BookStore.search_by_keyword(q)
    else:
        result = BookStore.search_by_isbn(q)

    return jsonify(result)