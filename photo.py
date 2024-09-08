#luggage-manager:photo 拍照功能

import os,libfile

def takephoto(itemid:int):
    '''拍照
itemid(int):物品id，用作文件名
需要在termux环境下运行'''
    if not os.getenv('TERMUX_VERSION'):
        print('非termux环境运行，跳过拍照')
        return
    filename = f'{libfile.IMG}/{itemid}.jpg'
    os.system(f'termux-camera-photo {filename}')
    __import__('imgcompress').compress((filename,))
