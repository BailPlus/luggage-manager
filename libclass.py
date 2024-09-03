#luggage-manager:libclass 类型模块

import libfile,libdebug
class Class:
    '''类别类
# 属性
- name(str):类别名称
- subclasses(list[int]):子类别id列表
- items(list[int]):属于该类别的物品id列表
- id(int):类别的hash值，自创建之后保持不变
# 方法
- add():向类别中添加物品
- addclass():向类别中添加子类别'''
    def __init__(self,name:str):
        '''name(str):类别名称'''
        self.name = name
        self.subclasses:list[int] = []
        self.items:list[int] = []
        self.id = hash(self)
        libfile.write(self)
    def __str__(self):
        return self.name
    def add(self,itemid:int):
        '''向类别中添加物品
itemid(int):物品对象id'''
        self.items.append(itemid)
        libfile.write(self)
        libdebug.debug(self.items)
    def addclass(self,classid:int):
        self.subclasses.append(classid)
        libfile.write(self)
class Item:
    '''物品类
# 属性
- name(str):物品名称
- place(int):物品放置位置对象id
- id(int):类别的hash值，自创建之后保持不变
# 方法
- moveto():移动物品到某一位置'''
    def __init__(self,name:str,placeid:int):
        '''name(str):物品名称
placeid(int):物品放置位置对象id，位置一般为容器类别下的物品'''
        self.name = name
        self.placeid = placeid
        self.id = hash(self)
        libfile.write(self)
    def __str__(self):
        return self.name
    def moveto(self,target:int):
        '''移动物品到某一位置
target(int):移动目标id'''
        self.placeid = target
        libfile.write(self,self.id)
