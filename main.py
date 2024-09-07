#!/usr/bin/python3
#Copyright Bail 2024
#luggage-namager 行李管家
#2024.8.26-2024.9.7

VERSION = 'v2.3'
VERCODE = 12
FUNCTIONS = ('test','add','newclass','cp','mv','rm','where','put')  # 功能列表，用于解析sys.argv[1]

import sys,os,libfile

def init():
    libfile.init()
def welcome():
    '''欢迎页'''
    print(f'行李管家 {VERSION}_{VERCODE}')
def help():
    print(FUNCTIONS)
def interactive():
    '''交互式运行'''
    while True:
        try:
            cmd = input('>')
        except (EOFError,KeyboardInterrupt):
            print() #防止在同一行显示提示符
            return
        if not cmd:
            continue
        if cmd in ('exit','quit','q'):
            return
        os.system(' '.join((sys.executable,sys.argv[0],cmd)))
def main():
    init()
    if len(sys.argv) == 1:  # 直接运行
        welcome()
        interactive()
    elif sys.argv[1] in ('help','-h','-help','--help'):
        help()
    else:   # 带参数运行
        func = sys.argv[1]
        if func in FUNCTIONS:
            __import__(func).main([] if len(sys.argv)==2 else sys.argv[2:])
        else:
            print('不存在的命令：'+func)
    return 0

if __name__ == '__main__':
    sys.exit(main())
