# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/18 15:43'



"""
关键字参数以及默认参数
"""


def func(a,b,c):
    print(a,b,c)

func(1,2,3)

# 关键字参数
func(c=3,b=2,a=1)


# 默认参数

def func1(a,b=100,c=200):
    print(a,b,c)

print("")
func1(90)

func1(90,9000)

# >>>
# 90 100 200
# 90 9000 200

func1(1,2,3)

# >>>
# 1 2 3

print("")
print("")
"""
关键字参数和默认参数的混合
"""

def func2(spam,eggs,toast=0,ham=0):
    print((spam,eggs,toast,ham))

func2(1,2)
print("")
func2(1,ham=1,eggs=0)
print("")
func2(spam=2,eggs=0)
print("")
func2(toast=1,eggs=2,spam=3)
print("")
print(1,2,3,4)
# >>>
# (1, 2, 0, 0)
#
# (1, 0, 0, 1)
#
# (2, 0, 0, 0)
#
# (3, 2, 1, 0)
#
# 1 2 3 4



















