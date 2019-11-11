#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 20:31
# @File    : Test_2.py


"""

给属性指定默认值

"""


class Car():
    
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color
        self.make = "China"  # 默认值
    
    def getCarMsg(self):
        print(self.name + "---" + str(self.price) + "---" + self.color 
              + "---" + self.make)
    
    

car1 = Car("大众",1000,"white")

car1.getCarMsg()
        
        
    
        