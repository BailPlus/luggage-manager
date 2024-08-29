#luggage-manager:add 物品注册功能

from libfile import *
import libdebug,os

nextids ={}

def help():
    print('''\
用法：luggage-manager add [<类别id> <物品名称> [选项]]

目前支持的选项：
--no-photo      不进行拍照''')
def interactive():
    '''交互式'''
    print('暂未开放')
def getid():
    '''获取下一个编号'''
    # 提取已注册的物品id
    with open(MANIFEST) as file:
        items = file.readlines()
    for i,j in enumerate(items):
        items[i] = j.split()[0]
    # 获取每一个类别中的最大值
    for i in items:
        recorded = nextids.get(i[:-2],'01') # 取已经记录的值，如果没有就是01
        new = hex(int(i[-2:],16)+1)[2:]     # 当前要记录的值。因为要获取的是“下一个”编号，所以+1。同时过滤hex()中默认存在的“0x” 
        if len(new) == 1:
            new = '0'+new
        elif new == 'ff':
            raise RuntimeError('溢出，暂时无法处理')
        nextids[i[:-2]] = max(recorded,new) # 取最大值进行记录
def register(classid:str,name:str)->str:
    '''向清单文件中注册
classid(str):该物品所属的类别
name(str):物品名称
返回值:新物品的id(str)'''
    # 获取物品id
    itemid = classid + nextids[classid]
    # 更新字典中的下一个id
    nextid = hex(int(itemid[-2:],16)+1)[2:]
    if len(nextid) == 1:
        nextid = '0'+nextid
    if nextid == 'ff':
        raise RuntimeError('溢出，暂时无法处理')
    nextids[classid] = nextid
    # 进行记录
    with open(MANIFEST,'a') as file:
        file.write(f'{itemid} {name} 1\n')
    return itemid
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
    getid()
    if not args:
        interactive()
    else:
        if '--help' in args:
            help()
        else:
            itemid = register(*args[:2])
            if '--no-photo' not in args:
                takephoto(itemid)
            print(f'注册成功！物品id：{itemid}')
