'a test module'

__author__ = 'suprecm'

import sys              #sys模块中有一个argv变量，可以用list存储命令行的所有参数，第一个永远是运行的.py文件

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello,world!')
    elif len(args) == 2:
        print('Hello %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
