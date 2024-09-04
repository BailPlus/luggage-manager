#luggage-manager:libchoose 选择和罗列模块

import libfile,libclass,libdebug

def choose_classid(parentid:int=libfile.rootclass.id)->int:
    '''引导用户选择类别id
parentid(int):已选择的父类别id
返回值:用户选择的子类别id(int)'''
    while True:
        classobj:libclass.Class = libfile.read(parentid) # type: ignore
        libdebug.debug(classobj.subclasses)
        # 显示子类别
        for i,j in enumerate(classobj.subclasses):
            print('\t'.join((str(i),str(libfile.read(j))+'/')))
            userinput = input('请选择一个类别，以空行结束 >')
            if userinput:
                parentid = classobj.subclasses[int(userinput)]
            else:
                break
    return parentid
def choose_class(parentid:int=libfile.rootclass.id)->libclass.Class:
    '''引导用户选择类别
parentid(int):已选择的父类别id
返回值:用户选择的子类别(libclass.Class)'''
    classid = choose_classid(parentid)
    classobj:libclass.Class = libfile.read(classid) # type: ignore
    return classobj
def choose_itemid(parentid:int=libfile.rootclass.id,isshowclass:bool=True)->int:
    '''引导用户选择物品id
parentid(int):已选择的父类别id
isshowclass(bool):是否显示子类别即是否允许进入子类别
返回值:用户选择的物品id(int)'''
    while True:
        classobj:libclass.Class = libfile.read(parentid) # type: ignore
        # 显示子类别
        if isshowclass:
            for i,j in enumerate(classobj.subclasses):
                print('\t'.join((str(i),str(libfile.read(j))+'/')))
        offset = len(classobj.subclasses) if isshowclass else 0
        # 显示类别下的物品
        for i,j in enumerate(classobj.items):
            print('\t'.join((str(i+offset),str(libfile.read(j)))))
        # 获取用户输入
        while True:
            try:
                userinput = int(input('请选择一个物品 >'))
            except Exception:
                print('输入有误，请重新输入')
            else:
                break
        # 处理子类别相关
        if userinput >= offset:
            break
        else:
            parentid = classobj.subclasses[userinput]
    return classobj.items[userinput-offset]
def choose_item(parentid:int=libfile.rootclass.id,isshowclass:bool=True)->libclass.Item:
    '''引导用户选择物品
parentid(int):已选择的父类别id
返回值:用户选择的物品(libclass.Class)'''
    itemid = choose_itemid(parentid,isshowclass)
    itemobj:libclass.Item = libfile.read(itemid) # type: ignore
    return itemobj
def choose_placeid()->int:
    '''引导用户选择放置处id
返回值:放置处id(int)
**从根类别下的“容器”类别中选择**
'''
    rootclass = libfile.rootclass
    for i in rootclass.subclasses:
        if str(libfile.read(i)) == '容器':
            container_classid = i
            break
    else:
        raise KeyError('找不到容器类')
    return choose_itemid(container_classid)
def choose_place()->libclass.Item:
    '''引导用户选择放置处
返回值:放置处(libclass.Item)
**从根类别下的“容器”类别中选择**
'''
    rootclass = libfile.rootclass
    for i in rootclass.subclasses:
        if str(libfile.read(i)) == '容器':
            container_class = i
        else:
            raise KeyError('找不到容器类')
    return choose_item(container_class)
