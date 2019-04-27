'''
图书数据获取api，基地址：http://t.yushu.im
关键字搜索：http://t.yushu.im/v2/book/search?q={}&start={}&end={}
isbn搜索：http://t.yushu.im/v2/book/isbn/{isbn}
'''

from flask import jsonify, request

from app.forms.book import SearchForm
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
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'key':
            result = BookStore.search_by_keyword(q, page)
        else:
            result = BookStore.search_by_isbn(q)

        return jsonify(result)
    else:
        return jsonify({'msg': form.errors})
