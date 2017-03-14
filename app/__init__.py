#!/usr/bin/env python
# coding=utf-8
"""
    @description: ??
    @author: calloy
    @contact: calloy2007@gmail.com
    @site: http://yooou.cn
    @file: __init__.py   17-3-4 下午2:46
"""

from flask import Flask
from .config import Default



def create_app():
    app = Flask(__name__)
    # load config
    app.config.from_object(Default)

    # register Blueprint
    from app.web import web as web_blueprint
    app.register_blueprint(web_blueprint)



    return app
#
# def create_app():
#     '''创建Flask APP'''
#     config = load_config()
#
#     app = Flask(__name__)
#     ## 加载配置文件
#     app.config.from_object(config)
#
#     # 注册组件
#     register_db(app)
#     register_jianjia(app)
#     register_route(app)
#     register_error_handle(app)
#     register_hooks(app)
#     db.init_app(app)
#     login_manager.init_app(app)
#     # 创建数据表
#     # db.drop_all()
#     # db.create_all()
#
#     return app
#
#
# def register_jianjia(app):
#     ''' jianjia2 模版 filter，vars,function '''
#     pass
#
# def register_db(app):
#     '''数据库db初始化'''
#     pass
#
# def register_route(app):
#     ''' 注册路由/蓝图'''
#     from app.admin import admin as admin_blueprint
#     app.register_blueprint(admin_blueprint,url_prefix='/admin')
#
# def register_error_handle(app):
#     '''注册HTTP错误页面'''
#
#     @app.errorhandler(403)
#     def page_403(error):
#         return render_template('error/403.html'), 403
#
#     @app.errorhandler(404)
#     def page_404(error):
#         return render_template('error/404.html'), 404
#
#     @app.errorhandler(500)
#     def page_500(error):
#         return render_template('error/500.html'), 500
#
# def register_hooks(app):
#     '''注册钩子'''
#     pass
