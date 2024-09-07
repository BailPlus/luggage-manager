#luggage-manager:put 放置或移动行李到某一容器

import libclass,libchoose

def put(item:libclass.Item,containerid:int):
    '''放置或移动行李到某一容器
item(libclass.Item):要放置的物品
containerid(int):要放置到的容器id'''
    item.moveto(containerid)
def main(*args):
    item = libchoose.choose_item()
    containerid = libchoose.choose_placeid()
    put(item,containerid)
    print('放置成功')
