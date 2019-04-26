from flask import Flask, jsonify

from app.bookstore.book import BookStore
from app.tools.helper import is_isbn_or_key

app = Flask(__name__)
# 要求配置中的变量名必须都大写
app.config.from_object('config')

'''
图书数据获取api，基地址：http://t.yushu.im
关键字搜索：http://t.yushu.im/v2/book/search?q={}&start={}&end={}
isbn搜索：http://t.yushu.im/v2/book/isbn/{isbn}
'''


@app.route('/book/search/<q>/<page>')
def search(q, page):
    '''
    :param q: 搜索关键字 or isbn
    :param page:
    :return:
    '''

    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'key':
        result = BookStore.search_by_keyword(q)
    else:
        result = BookStore.search_by_isbn(q)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])
