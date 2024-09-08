#luggage-manager:add 物品注册功能

from libfile import *
import libdebug,os,libclass,libchoose,photo

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
    itemclass:libclass.Class = read(itemclassid) # type: ignore
    # 选择容器
    if iscontainer:
        placeid = libchoose.choose_placeid()
    # 创建对象
    item = libclass.Item(name,placeid if iscontainer else 0)
    itemclass.add(item.id)
    return item.id
def main(args):
    if not args:
        interactive()
    else:
        if '--help' in args:
            help()
        else:
            itemid = add(args[0],False if '--no-container' in args else True)
            if '--no-photo' not in args:
                photo.takephoto(itemid)
            print('注册成功！')
