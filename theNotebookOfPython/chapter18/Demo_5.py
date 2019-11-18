# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/18 16:07'


"""
keyword-only 参数
"""

# 出现在参数列表中*args之后，所有参数必须在调用中使用关键字语法来传递

def func1(a,*args,c):
    print((a,args,c))
    print("")

func1(1,c=2)
# >>>
# (1, (), 2)

func1(1,2,3,c=100)
# >>>
# (1, (2, 3), 100)

# func1(1,3)
# >>>
# TypeError: func1() missing 1 required keyword-only argument: 'c'


# 也可以单独使用*

def kwonly(a,*,c,d):
    print((a,c,d))
    print("")

kwonly(1,c=100,d=1000)
# >>>
# (1, 100, 1000)

# kwonly(1,23,2)
# >>>
# TypeError: kwonly() takes 1 positional argument but 3 were given


# 仍然可以对keyword-only参数使用默认值

def func2(a,*,c=1,d=100):
    print(a,c,d)
    print("")

func2(1)
# >>>
# 1 1 100

func2(1,c=1000)
# >>>
# 1 1000 100




