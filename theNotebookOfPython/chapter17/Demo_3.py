# -*- coding: utf-8 -*-
# @Time  : 2019/11/17 20:35
# @Author : Mr.Lin


"""
嵌套作用域和Lambda

"""


def func():
    x = 4
    action = (lambda n : x**n)
    return action

x = func()
print(x(2))
# >>>
# 16