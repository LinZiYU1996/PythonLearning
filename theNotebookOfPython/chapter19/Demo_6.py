# -*- coding: utf-8 -*-
# @Time  : 2019/11/18 23:11
# @Author : Mr.Lin

"""
函数式编程
"""

# 函数式编程就是对序列应用一些函数的工具

print(list(range(-5,5)))
print("")
# >>>
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

print(list(filter((lambda x : x > 0),range(-5,5))))
# >>>
# [1, 2, 3, 4]



from functools import reduce
print("")
print(reduce((lambda x,y : x + y),[1,2,3,4]))
# >>>
# 10
print("")
print(reduce((lambda x,y : x * y),[1,2,3,4]))
# >>>
# 24






















