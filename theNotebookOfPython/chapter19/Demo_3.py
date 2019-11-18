# -*- coding: utf-8 -*-
# @Time  : 2019/11/18 21:11
# @Author : Mr.Lin

"""
跳转表

"""


L = [
    lambda x : x ** 2,
    lambda x : x ** 3,
    lambda x : x ** 4,
]

for f in  L :
    print(f(2))

# >>>
# 4
# 8
# 16

print(L[0](3))
# >>>
# 9





