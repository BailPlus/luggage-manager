#!/usr/bin/python3
#Copyright Bail 2024
#imgcompress 图片压缩 v1.2.2_5
#2024.8.12-2024.8.29

WIDTH = 500 # 压缩后图像的宽度
QUALITY = 10    # 压缩后的图像品质

from PIL import Image
import os,sys

def getarg()->list[str]:
    '''获取图片路径
返回值:图片路径(syr)'''
    if len(sys.argv) == 1:
        files = os.listdir('img')
        for i,j in enumerate(files):
            files[i] = os.path.join('img',j)
    else:
        files = sys.argv[1:]
    return files
def compress(files:list[str],width:int=WIDTH,quality:int=QUALITY):
    '''处理图片
files(list[str]):要处理的文件列表
width(int)处理后的图片宽度，若为0则宽度不变'''
    for i in files:
        img = Image.open(i)
        if WIDTH:   # 如果WIDTH设为0则不进行缩放
            img = img.resize((WIDTH, int(img.size[1] * WIDTH / img.size[0])))
        img.save(i,'JPEG',quality=QUALITY)
def main():
    compress(getarg())
