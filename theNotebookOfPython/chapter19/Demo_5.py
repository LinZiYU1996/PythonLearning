# -*- coding: utf-8 -*-
# @Time  : 2019/11/18 23:04
# @Author : Mr.Lin


"""
序列中映射函数 map
"""

# map函数会对一个序列对象中的每一个元素应用被传入的函数
# 并且返回一个包含了所有函数调用结果的一个列表

def inc(x):
    return x + 10

counters = [1,2,3,4,5]
# print(list(map(inc,counters)))
# >>>
# [11, 12, 13, 14, 15]

# 使用lambda

print(list(map((lambda x : x+3),counters)))
# >>>
# [4, 5, 6, 7, 8]


print(pow(2,3))
# >>>
# 8

print(list(map(pow,[1,2,3],[4,5,6])))
# >>>
# [1, 32, 729]


































