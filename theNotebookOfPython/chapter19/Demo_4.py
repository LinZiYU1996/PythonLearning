# -*- coding: utf-8 -*-
# @Time  : 2019/11/18 22:58
# @Author : Mr.Lin

"""
嵌套Lambda和作用域
"""

def action(x):
    return (lambda y: x+y)

act = action(99)

# 嵌套的lambda能够获取到上层函数作用域中的变量x的值
print(act)
print("")
print(act(2))
# >>>
# <function action.<locals>.<lambda> at 0x0000025569377620>
#
# 101



























































