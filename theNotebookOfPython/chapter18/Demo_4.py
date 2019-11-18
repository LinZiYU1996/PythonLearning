# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/18 15:57'



"""
解包参数
"""

def func(a,b,c,d):
    print(a,b,c,d)

args = (1,2)
args += (3,4)
func(*args)
# >>>
# 1 2 3 4







