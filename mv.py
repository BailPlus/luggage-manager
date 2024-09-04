#luggage-manager:mv 移动物品

import libchoose,libclass,libfile

def move(itemid:int,origin:libclass.Class,dest:libclass.Class):
    '''移动物品到新的类型
itemid(int):你是谁
origin(libclass.Class):来自何方
dest(libclass.Class):又去往何处'''
    origin.remove(itemid)
    dest.add(itemid)
def main(*args):
    print('请选择要移动的物品所在类别')
    originid = libchoose.choose_classid()
    origin:libclass.Class = libfile.read(originid) # type: ignore
    print('请选择要移动的物品')
    itemid = libchoose.choose_itemid(originid)
    print('请选择要移动到的类别')
    dest = libchoose.choose_class()
    move(itemid,origin,dest)
    print('移动成功')
