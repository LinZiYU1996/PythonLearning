# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/17 16:52'

from array import array
import math

class Vector2d:

    typecode = 'd'

    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)


    def __iter__(self):
        return ( i for i in (self.x,self.y))



    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name,*self)


    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
        bytes(array(self.typecode, self)))


    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))



# ❶ Vector2d 实例的分量可以直接通过属性访问（无需调用读值方法）。
# ❷ Vector2d 实例可以拆包成变量元组。
# ❸ repr 函数调用 Vector2d 实例，得到的结果类似于构建实例的源码。
# ❹ 这里使用 eval 函数，表明 repr 函数调用 Vector2d 实例得到的是对构造方法的准确
# 表述。
# 这里使用 eval 函数克隆对象是为了说明 repr 方法。使用 copy.copy 函数克隆实例更安全也更快速。
# ❺ Vector2d 实例支持使用 == 比较；这样便于测试。
# ❻ print 函数会调用 str 函数，对 Vector2d 来说，输出的是一个有序对。
# ❼ bytes 函数会调用 __bytes__ 方法，生成实例的二进制表示形式。
# ❽ abs 函数会调用 __abs__ 方法，返回 Vector2d 实例的模。
# ❾ bool 函数会调用 __bool__ 方法，如果 Vector2d 实例的模为零，返回 False，否则
# 返回 True。

v1 = Vector2d(3,4)
print(v1.x,v1.y)
# >>>
# 3.0 4.0

print("")

x,y = v1

print(x,y)
# >>>
# 3.0 4.0
print("")

print(v1)

v1_clone = eval(repr(v1))

print(v1 == v1_clone)
# >>>
# True

print("")

octets = bytes(v1)

print(octets)
# >>>
# b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'



