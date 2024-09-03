#luggage-manager:libfile 文件相关库

from os.path import join
import os,pickle,libclass

PREFIX = os.path.expanduser('~/.config/luggage-manager')
LUGGAGE = join(PREFIX,'luggage')    # 行李目录
MANIFEST = join(LUGGAGE,'manifest.csv') # 清单文件
IMG = join(LUGGAGE,'img')   # 图片库
OBJ = join(LUGGAGE,'objects')   # 对象库
ROOTCLASSIDPATH = join(OBJ,'rootclassid')
rootclass:libclass.Class = None

def init():
    for i in (LUGGAGE,IMG,OBJ):
        os.makedirs(i) if not os.path.exists(i) else None
    for i in ():
        open(i,'a').close()

    global rootclass
    if not os.path.exists(ROOTCLASSIDPATH):
        rootclass = libclass.Class('root')
        container = libclass.Class('容器')
        rootclass.addclass(container.id)
        with open(ROOTCLASSIDPATH,'w') as file:
            file.write(str(rootclass.id))
    else:
        with open(ROOTCLASSIDPATH) as file:
            rootclass = read(int(file.read()))
def read(id:int)->object:
    '''读取对象
id(int|str):对象的id，即先前算出的hash值
返回值:这个对象(object)'''
    with open(join(OBJ,str(id)),'rb') as file:
        obj = pickle.load(file)
    return obj
def write(obj:object)->int:
    '''写入对象
obj(object):要写入的对象
返回值:该对象的id（hash值）(int)'''
    with open(join(OBJ,str(obj.id)),'wb') as file:
        pickle.dump(obj,file)
    return id
