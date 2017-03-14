#!/usr/bin/env python
# coding=utf-8
"""
    @description: 前端页面
    @author: calloy
    @contact: calloy2007@gmail.com
    @site: http://www.yooou.cn
    @file: home.py   17-3-6 下午8:45
"""
from . import web,music
from flask import render_template,current_app
import json




# web index  (/ or /index)
@web.route('/')
def index():
    print(current_app.config['Y_VERSION'])
    return render_template('index.html',version=current_app.config['Y_VERSION'])

@web.route('/music/index')
def music_index():
    return render_template('music_index.html')
@web.route('/music/player')
def music_player():
    print('start play music!')
    music.player()
    return '200'

@web.route('/music/music_info')
def music_info():
    return json.dumps(music.get_info())

@web.route('/music/stop')
def music_stop():
    music.stop()
    return '200'

@web.route('/music/next')
def music_next():
    music.next()
    return '200'

@web.route('/music/change/<channels>')
def music_change(channels):
    music.change_channel(channel=channels)
    return '200'