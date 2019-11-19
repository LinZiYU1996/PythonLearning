# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/19 16:37'



"""
砖石问题
"""

class BaseClass:

    num_base_calls = 0

    def call_me(self):
        print("Call me --------> Base")
        self.num_base_calls += 1



class LeftSubClass(BaseClass):

    num_left_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Left me --------------> Left")
        self.num_left_calls += 1




class RightSubClass(BaseClass):

    num_right_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print("Right me --------------> Right")
        self.num_right_calls += 1



class SubClass(LeftSubClass,RightSubClass):

    num_sub_calls = 0

    def call_me(self):

        LeftSubClass.call_me(self)

        RightSubClass.call_me(self)

        print("SUB ---------------> sub")

        self.num_sub_calls += 1

s = SubClass()
s.call_me()
print(s.num_sub_calls,s.num_left_calls,s.num_right_calls,s.num_base_calls)
# >>>
# Call me --------> Base
# Left me --------------> Left
# Call me --------> Base
# Right me --------------> Right
# SUB ---------------> sub
# 1 1 1 2

# 问题：
#     基类 call me 被调用了两次





























































