# -*- coding: utf-8 -*-
# @Time  : 2019/11/18 21:04
# @Author : Mr.Lin

"""

Lambda
"""

def func(x,y,z):
    return x*y*z

print(func(1,3,5))
print("")
f = lambda x,y,z:x*y*z
print(f(1,3,5))

# 使用默认参数

xx = (lambda a='a',b='c',c='d':a+b+c)
print(xx("asas"))

# >>>
# 15
#
# 15
# asascd



























































