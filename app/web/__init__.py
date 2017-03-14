#!/usr/bin/env python
# coding=utf-8
"""
    @description: ??
    @author: calloy
    @contact: calloy2007@gmail.com
    @site: http://www.yooou.cn
    @file: __init__.py   17-3-6 下午9:23
"""

from flask import Blueprint
from ..modes.music import Music

# register blueprint
web = Blueprint('web',__name__)

# register modes
music = Music()
from . import admin,home
