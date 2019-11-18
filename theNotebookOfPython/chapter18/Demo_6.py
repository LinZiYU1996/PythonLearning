# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/18 16:25'


"""
函数任务
能够计算任意参数集合和任意对象数据类型集合中的最小值
"""
def min1(*args):
    res = args[0]
    for arg in args:
        if arg < res:
            res = arg
    return res


def min2(first,*args):
    for arg in args:
        if arg < first:
            first = arg
    return first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print(min(3,4,1,101,9))
print("")
print(min2("bb","aa","cc"))
print("")
print(min3([2,2],[3,3],[1,1]))
# >>>
# 1
#
# aa
#
# [1, 1]


















