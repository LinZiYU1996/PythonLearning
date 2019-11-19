# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/19 16:55'


"""
对于demo3的砖石问题的改进
"""

class BaseClass:

    num_base_calls = 0

    def call_me(self):
        print("Call me --------> Base")
        self.num_base_calls += 1



class LeftSubClass(BaseClass):

    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("Left me --------------> Left")
        self.num_left_calls += 1




class RightSubClass(BaseClass):

    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("Right me --------------> Right")
        self.num_right_calls += 1



class SubClass(LeftSubClass,RightSubClass):

    num_sub_calls = 0

    def call_me(self):

        super().call_me()

        print("SUB ---------------> sub")

        self.num_sub_calls += 1

s = SubClass()
s.call_me()
print(s.num_sub_calls,s.num_left_calls,s.num_right_calls,s.num_base_calls)


# >>>
# Call me --------> Base
# Right me --------------> Right
# Left me --------------> Left
# SUB ---------------> sub
# 1 1 1 1















































































