#luggage-manager:add 物品注册功能

from libfile import *
import libdebug,os,libclass,libchoose

nextids = {}

def help():
    print('''\
用法：luggage-manager add [<物品名称> [选项]]

目前支持的选项：
--no-photo      不进行拍照''')
def interactive():
    '''交互式'''
    name = input('请输入物品名称 >')
    main((name,))
def add(name:str,iscontainer:bool)->int:
    '''新增物品。传入物品名称，然后引导用户选择类别以及放置地点
name(str):物品名称
iscontainer(bool):是否添加容器
返回值:物品id(int)'''
    # 选择类别
    itemclassid = libchoose.choose_classid()
    itemclass:libclass.Class = read(itemclassid)
    # 选择容器
    if iscontainer:
        placeid = libchoose.choose_placeid()
    # 创建对象
    item = libclass.Item(name,placeid if iscontainer else 0)
    itemclass.add(item.id)
def takephoto(itemid:int):
    '''拍照
itemid(int):物品id，用作文件名
需要在termux环境下运行'''
    if not os.getenv('TERMUX_VERSION'):
        print('非termux环境运行，跳过拍照')
        return
    filename = f'{IMG}/{itemid}.jpg'
    os.system(f'termux-camera-photo {filename}')
    __import__('imgcompress').compress((filename,))
def main(args):
    if not args:
        interactive()
    else:
        if '--help' in args:
            help()
        else:
            itemid = add(args[0],False if '--no-container' in args else True)
            if '--no-photo' not in args:
                takephoto(itemid)
            print('注册成功！')
