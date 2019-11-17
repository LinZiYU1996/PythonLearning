# -*- coding: utf-8 -*-
# @Time  : 2019/11/17 20:29
# @Author : Mr.Lin




"""
嵌套作用域
"""

x =99

def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()
# >>>
# 88
# f2是f1本地作用域内的一个本地变量





