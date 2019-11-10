#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 20:00
# @File    : Test1.py

"""
函数的简单使用
"""


# 传递参数到函数中
def greet(Msg):
    print(Msg)


greet("Hello World")



print("---------------------------------")
# 使用默认值
def function(person_name,age=18):
    print(person_name + "+"+ str(age))

#缺省使用默认值
function("hello")

#给定参数直接使用
function("pll",90)




print("---------------------------------")


#函数返回值

def re_func(name1,name2):
    name = name1 + name2
    # print(name.title())#首字母大写
    return name.title()

the_name = re_func("aadddj","hddhdh")
print(the_name)




print("---------------------------------")


# 传递列表给函数

def deal_List(Lists):
    for i in Lists:
        print(i)

a_List = [1,2,3,4,5,6]

deal_List(a_List)

print("---------------------------------")

# 传递任意数量的实参

def make_meal(*options):#(参数元组形式)
    print(options)


make_meal('bread')
make_meal('bread','apple')
make_meal('bread','apple','pear')


