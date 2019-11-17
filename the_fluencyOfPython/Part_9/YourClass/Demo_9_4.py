# -*- coding: utf-8 -*-
# @Time  : 2019/11/17 19:15
# @Author : Mr.Lin



class Demo:

    @classmethod
    def klassmeth(*args):
        return args


    @staticmethod
    def statmeth(*args):
        return args


# ❶ klassmeth 返回全部位置参数。
# ❷ statmeth 也是。
# ❸ 不管怎样调用 Demo.klassmeth，它的第一个参数始终是 Demo 类。
# ❹ Demo.statmeth 的行为与普通的函数相似。
print(Demo.klassmeth())
# >>>
# (<class '__main__.Demo'>,)
print("")

print(Demo.klassmeth('pattem'))
# >>>
# (<class '__main__.Demo'>, 'pattem')

print("")

print(Demo.statmeth())
# >>>
# ()

print("")
print(Demo.statmeth('pattem'))
# >>>
# ('pattem',)




