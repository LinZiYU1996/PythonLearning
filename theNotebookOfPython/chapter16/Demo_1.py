# -*- coding: utf-8 -*-
# @Time  : 2019/11/17 19:59
# @Author : Mr.Lin


"""
python中的多态
依赖类型的行为
一个操作的意义取决于被操作对象的类型



"""

def times(x,y):
    return x*y


print(times(2,4))
# >>>
# 8

print("")

print(times('NI',4))
# >>>
# NINININI

# 对比,可以看出函数的作用不同

# 函数times的作用取决于传递给它的值




