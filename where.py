#luggage-manager:where 查找物品放置位置

import libchoose,libfile,libclass,libdebug

def main(*args):
    print('请选择要查询的物品')
    item = libchoose.choose_item()
    libdebug.debug(item)
    libdebug.debug(item.placeid)
    if not item.placeid:
        print('该物品没有存放位置')
        return
    place:libclass.Item = libfile.read(item.placeid) # type: ignore
    print(place.name)
