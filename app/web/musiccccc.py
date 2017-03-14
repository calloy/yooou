#!/usr/bin/env python
# coding=utf-8
"""
    @description: ??
    @author: calloy
    @contact: calloy2007@gmail.com
    @site: http://yooou.cn
    @file: music.py   17-2-9 下午2:43
"""

import subprocess
import time
import requests
from flask import Flask, render_template
import threading

p = None
stats = 'stop'
threds = []
channel = 'public_tuijian_rege'


def geturl(channel):
    music_url = 'http://api.jirengu.com/fm/getSong.php'
    # http: // api.jirengu.com / fm / getSong.php?channel = public_tuijian_rege & version = 100 & type = n
    # payload = {'channel': 'public_shiguang_jingdianlaoge', 'version': '100', 'type': 'n'}
    payload = {'channel': channel, 'version': '100', 'type': 'n'}
    r = requests.get(music_url, params=payload)
    url_json = r.json()
    return url_json['song'][0]['url']


def play(filename):
    global p
    # stop()
    p = subprocess.Popen(['mpg123', filename])
    p.wait()


def stop():
    global p
    if p:
        p.terminate()
        p = None


def run():
    global stats
    global channel
    while stats == 'play':
        url = geturl(channel)
        play(url)
        time.sleep(2)


def api_run():
    app = Flask(__name__)
    return app


application = api_run()


def musicplay():
    global stats
    run_forever = True
    while run_forever:
        t1 = None
        if stats == 'run':
            print('run-1')
            print(stats)
            stats = 'play'  # 改变播放状态为播放play，避免多次运行线程
            t1 = threading.Thread(target=run)
            # t1.setDaemon(True)
            t1.start()
        elif stats == 'stop':  # 结束循环
            print('stop-1')
            print(stats)
            stop()
            # t2 = threading.Thread(target=stop())
            # t2.setDaemon(True)
            # t2.run()
            run_forever = False


# 播放音乐
@application.route('/player')
def player():
    global stats
    global channel
    channel = 'public_tuijian_rege'
    if (stats == 'stop'):  # 防止重复运行
        stats = 'run'
        top = threading.Thread(target=musicplay)
        threds.append(top)
        top.start()
    return '200'


# 停止播放
@application.route('/stop')
def stopmusic():
    global stats
    stats = 'stop'
    return '200'


# 切换频道
@application.route('/change/<channels>')
def change(channels):
    print('channel')
    print(channels)
    global channel
    global stats
    channel = channels
    stats = 'stop'
    time.sleep(3)
    if (stats == 'stop'):  # 防止重复运行
        stats = 'run'
        top = threading.Thread(target=musicplay)
        threds.append(top)
        top.start()
    return '200'


# 下一首
@application.route('/next')
def next():
    global stats
    if stats == 'stop':
        return '400'
    stats = 'stop'
    time.sleep(3)
    if (stats == 'stop'):  # 防止重复运行
        stats = 'run'
        top = threading.Thread(target=musicplay)
        threds.append(top)
        top.start()
    return '200'


@application.route('/')
def index():
    return render_template('index.html')
