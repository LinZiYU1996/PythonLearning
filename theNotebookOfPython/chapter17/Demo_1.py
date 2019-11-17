# -*- coding: utf-8 -*-
# @Time  : 2019/11/17 20:21
# @Author : Mr.Lin



"""
global语句

"""


a =11

def func():
    global a
    a = 100

func()
print(a)

# >>>
# 100