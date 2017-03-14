#!/usr/bin/env python
# coding=utf-8
"""
    @description: 启动文件
    @author: calloy
    @contact: calloy2007@gmail.com
    @site: http://yooou.cn
    @file: manage.py   17-3-4 下午2:39
"""
from app import create_app

def run_app():
    app = create_app()
    return app
    # app.run()

app = run_app()

if __name__ == '__main__':
    pass