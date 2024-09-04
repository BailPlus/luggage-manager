#luggage-manager:cp 复制物品

import libchoose,libclass

def move(itemid:int,dest:libclass.Class):
    '''复制物品到新的类型
itemid(int):要复制的物品id
dest(libclass.Class):复制的去向'''
    dest.add(itemid)
def main(*args):
    print('请选择要复制的物品')
    itemid = libchoose.choose_itemid()
    print('请选择要移动到的类别')
    dest = libchoose.choose_class()
    move(itemid,dest)
    print('移动成功')
