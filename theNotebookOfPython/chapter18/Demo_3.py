# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/18 15:50'




"""
任意参数
"""

def f(*args):
    print(args)
    print("")

f()

f(1)

f(1,2,3,4)

# >>>
# ()
#
# (1,)
#
# (1, 2, 3, 4)


"""
**特性
"""
def f1(**kwargs):
    print(kwargs)
    print("")

f1()

f1(a=1,b=2,c=3)

# >>>
# {}
#
# {'a': 1, 'b': 2, 'c': 3}


# 三种混合

def f2(a,*args,**kwargs):
    print(a,args,kwargs)

f2(1,2,3,x=1,y=2)
# >>>
# 1 (2, 3) {'x': 1, 'y': 2}






