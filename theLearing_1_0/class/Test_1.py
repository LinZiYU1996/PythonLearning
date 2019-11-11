#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 20:19
# @File    : Test_1.py


"""
类的实用
"""



"""
以self为前缀的变量都可以供类中的所有方法使用
还可以通过类的任何实例来访问这些变量


"""
class Dog():

    def __init__(self,name,age):
        self.name = name
        self.age = age


    def sit(self):
        print(self.name + "   is sitting")

    def roll_over(self):
        print(self.name + "   is roll over")



myDog = Dog("a",1929)

myDog.sit()

myDog.roll_over()


