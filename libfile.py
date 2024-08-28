#luggage-manager:libfile 文件相关库

from os.path import join
import os

PREFIX = os.path.expanduser('~/.config/luggage-manager')
LUGGAGE = join(PREFIX,'luggage')    # 行李目录
MANIFEST = join(LUGGAGE,'manifest.csv') # 清单文件
IMG = join(LUGGAGE,'img')   # 图片库

def init():
    for i in (LUGGAGE,IMG):
        os.makedirs(i) if not os.path.exists(i) else None
    for i in (MANIFEST,):
        open(i,'a').close()
