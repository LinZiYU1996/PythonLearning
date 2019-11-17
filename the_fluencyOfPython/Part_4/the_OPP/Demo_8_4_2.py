# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/17 16:32'

"""
如果定义的函数接收可变参数，应该谨慎考虑调用方是否期望修改传入的参数。
例如，如果函数接收一个字典，而且在处理的过程中要修改它，那么这个副作用要不要体
现到函数外部？具体情况具体分析。这其实需要函数的编写者和调用方达成共识
"""
class TwilightBus:

    def __init__(self,passengers = None):

        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self,name):
        self.passengers.append(name)


    def drop(self,name):
        self.passengers.remove(name)

























