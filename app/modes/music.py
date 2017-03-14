#!/usr/bin/env python
# coding=utf-8
"""
    @description: 音乐播放模块
    @author: calloy
    @contact: calloy2007@gmail.com
    @site: http://yooou.cn
    @file: music.py   17-3-4 下午2:47
"""
import requests
import threading
import time
import subprocess

class Music(object):

    def __init__(self):
        self._baseUrl = 'http://api.jirengu.com/fm/getSong.php'
        self._musicInfo = {}                                  # 音乐信息
        self.channel = 'public_tuijian_rege'                    # 默认播放频道
        self._stateInfo = {'state':'stop','play':'stop'}
        self._threds = []
        self._p = None                                          # mpg123运行后的进程信息
        # 错误声音地址
        self._errPath = 'http://telecom.26923.com/2014/ring/000/104/4e9ec903904d09813594a0f5488c8572.mp3'

    def init_app(self):
        pass
    def _getMusicUrl(self):
        '''
        获取音乐地址
        :return: True/False
        '''
        payload = {'channel': self.channel, 'version': '100', 'type': 'n'}
        try:
            r = requests.get(self._baseUrl,params=payload)
        except:
            return False
        url_json = r.json()
        if len(url_json):
            self._musicInfo = url_json['song'][0]
            print('get new music url success!')
            return True
        else:
            return True

    def _play(self,filename):
        '''
        使用mpg123播放音乐，树莓派现在只能mpg123
        :param filename:音乐URL
        :return:
        '''
        self._stateInfo['play'] = 'playing'
        print('start play:'+self._musicInfo['title'])
        self._p = subprocess.Popen(['mpg123', filename])
        self._p.wait()
        print(self._musicInfo['title']+' - play end!')
        self._stateInfo['play'] = 'play'
    def _stop(self):
        '''
        结束现在正在使用的mpg123进程
        :return:
        '''
        if self._p :
            self._p.terminate()
            self._p = None
        print('terminate play')

    def _run(self):
        while self._stateInfo['state'] == 'play':
            if self._stateInfo['play'] == 'playing':
                continue
            if self._getMusicUrl():
                self._play(self._musicInfo['url'])
                time.sleep(2)
            else: # 获取新的url失败，直接播放错误声音
                self._play(self._errPath)


    def _player(self):
        '''
        按上次/默认播放音乐
        :return:
        '''
        # 通过state控制重复运行----state只有两种状态 stop and play
        if self._stateInfo['state'] == 'stop':
            self._stateInfo['state'] = 'play'
        elif self._stateInfo['state'] == 'play':
            return
        run_forever = True
        while run_forever:
            if self._stateInfo['state'] == 'play':
                # 播放音乐
                # 结束后 获取新的音乐
                # 继续播放
                if self._stateInfo['play'] == 'stop':
                    # 只有在程序由停止状态转为播放状态的时候才执行，在程序结束播放的时候恢复标识为stop
                    self._stateInfo['play'] = 'play'
                    t1 = None
                    t1 = threading.Thread(target=self._run)
                    t1.start()
            elif self._stateInfo['state'] == 'stop':
                # 结束当前正在播放的音乐,退出播放循环
                self._stop()
                run_forever = False

    def player(self):
        '''
        外部调用接口，播放音乐.
        :return:
        '''
        # 只有当state是stop的情况下才允许播放
        if self._stateInfo['state'] == 'stop':
            top = threading.Thread(target=self._player)
            self._threds.append(top)
            top.start()
            return True
        else:
            return False

    def next(self):
        '''
        下一曲
        :return:
        '''
        print('next')
        self._stateInfo['state'] = 'stop'
        time.sleep(4)
        self._stateInfo['play'] = 'stop'
        if self._stateInfo['state'] == 'stop':
            top = threading.Thread(target=self._player)
            self._threds.append(top)
            top.start()
            return True
        else:
            return False


    def stop(self):
        '''
        停止播放
        :return:
        '''
        self._stateInfo['state'] = 'stop'
        self._stateInfo['play'] = 'stop'
        self._musicInfo['title'] = '---'
        return True


    def change_channel(self,channel):
        '''
        切换播放频道
        :param channel: 频道ID
        :return:
        '''
        print('change channel')
        self._stateInfo['state'] = 'stop'
        self.channel = channel
        time.sleep(4)
        self._stateInfo['play'] = 'stop'
        if self._stateInfo['state'] == 'stop':
            top = threading.Thread(target=self._player)
            self._threds.append(top)
            top.start()
            return True
        else:
            return False


    def get_info(self):
        info=self._musicInfo
        info['channel'] = self.channel
        return info

