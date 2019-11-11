# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/11 14:27'


"""
装饰器基础知识
"""

def deco(func):
    def inner():
        print("running inner()")

    return inner()

@deco
def targer():
    print("running targer")


"""
targer现在是inner的引用

"""
targer