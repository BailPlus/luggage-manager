#luggage-manager:libchoose 选择和罗列模块

import libfile,libclass,libdebug

def choose_classid(parentid:int=libfile.rootclass.id)->int:
    '''引导用户选择类别id
parentid(int):已选择的父类别id
返回值:用户选择的子类别id(int)'''
    while True:
        classobj:libclass.Class = libfile.read(parentid)
        libdebug.debug(classobj.subclasses)
        for i,j in enumerate(classobj.subclasses):
            print('\t'.join((str(i),str(libfile.read(j)))))
        userinput = input('请选择一个类别，以空行结束 >')
        if userinput:
            parentid = classobj.subclasses[int(userinput)]
        else:
            break
    return parentid
def choose_class(parentid:int)->libclass.Class:
    '''引导用户选择类别
parentid(int):已选择的父类别id
返回值:用户选择的子类别(libclass.Class)'''
    classid = choose_classid(parentid)
    classobj = libfile.read(classid)
    return classobj
def choose_itemid(parentid:int)->int:
    '''引导用户选择物品id
parentid(int):已选择的父类别id
返回值:用户选择的物品id(int)'''
    while True:
        classobj:libclass.Class = libfile.read(parentid)
        for i,j in enumerate(classobj.subclasses):
            print('\t'.join((str(i),str(libfile.read(j)))))
        for i,j in enumerate(classobj.items):
            print('\t'.join((str(i),str(libfile.read(j)))))
        userinput = int(input('请选择一个物品 >'))
        if userinput >= len(classobj.subclasses):
            break
    return classobj.items[userinput-len(classobj.subclasses)]
def choose_item(parentid:int)->libclass.Item:
    '''引导用户选择物品
parentid(int):已选择的父类别id
返回值:用户选择的物品(libclass.Class)'''
    itemid = choose_itemid(parentid)
    itemobj = libfile.read(itemid)
    return itemobj
def choose_placeid()->int:
    '''引导用户选择放置处id
返回值:放置处id(int)
**从根类别下的“容器”类别中选择**
'''
    rootclass = libfile.rootclass
    for i in rootclass.subclasses:
        if str(libfile.read(i)) == '容器':
            container_class = i
            break
    else:
        raise KeyError('找不到容器类')
    return choose_itemid(container_class)
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
