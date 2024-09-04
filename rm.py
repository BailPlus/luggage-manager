#luggage-manager:rm 删除物品

import libchoose,libclass,libfile

def remove(itemid:int,origin:libclass.Class):
    origin.remove(itemid)
def main(*args):
    print('请选择要移动的物品所在类别')
    originid = libchoose.choose_classid()
    origin:libclass.Class = libfile.read(originid) # type: ignore
    print('请选择要移动的物品')
    itemid = libchoose.choose_itemid(originid)
    remove(itemid,origin)
    print('移除成功')
