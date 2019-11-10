#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 20:38
# @File    : Test_3.py


"""

继承

"""


class Car():

    def __init__(self,name,price):

        self.name = name

        self.price = price

    def getMsg(self):

        print(self.name + "---+" + str(self.price))



class BenzCar(Car):

    def __init__(self,name,price):
        # super帮助将父类和子类关联起来
        super().__init__(name,price)



benz = BenzCar("benz",122)

benz.getMsg()


class M_Car(Car):

    def __init__(self,name,price):
        super().__init__(name,price)

        #给子类添加属性
        self.model = "YUan"

    def getMsg(self):

        print(self.name + self.model)


mcar = M_Car("M",183883)

mcar.getMsg()