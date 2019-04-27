from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.settings')
    register_blueprint(app)

    # 注册sqlalchemy数据库
    db.init_app(app)
    # 创建数据表
    db.create_all(app=app)

    return app


def register_blueprint(app):
    from app.webviews.web import web
    app.register_blueprint(web)