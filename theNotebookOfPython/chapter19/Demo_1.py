# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/18 16:42'

"""
间接函数调用
"""

# 把函数看做对象

# 函数名直接是一个对象的引用

# 可以自由的把这个对象赋值给其他的名称并且调用它


def echo(msg):
    print(msg)

x = echo
x('a')


def inderict(func,arg):
    func(arg)

inderict(echo,'a')


print("")
list = [(echo,'a'),(echo,'b')]
for (func,arg) in list:
    func(arg)

# >>
# a
# b














