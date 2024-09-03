#luggage-manager:newclass 新增类别

import libchoose,libclass,libfile

def help():
    print('''\
用法：luggage-manager newclass [类别名称]
''')
def interactive():
    name = input('请输入类别名称 >')
    main((name,))
def add(name:str)->int:
    '''增加类别
name(str):类别名称
返回值:类别id(int)'''
    classobj = libclass.Class(name)
    classobj.id = hash(classobj)
    libfile.write(classobj)
    parentid = libchoose.choose_classid()
    parent:libclass.Class = libfile.read(parentid)
    parent.addclass(classobj.id)
def main(args):
    if not args:
        interactive()
    else:
        if '--help' in args:
            help()
        else:
            name = args[0]
            add(name)
            print('添加成功')
