# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/17 16:19'

"""
不要使用可变类型作为参数的默认值
"""

"""
可选参数可以有默认值，这是 Python 函数定义的一个很棒的特性，这样我们的 API 在进
化的同时能保证向后兼容。然而，我们应该避免使用可变的对象作为参数的默认值。
"""
class HauntedBus:

    def __init__(self,passengers=[]):
        self.passengers = passengers

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice','Bill'])
print(bus1.passengers)
# >>>
# ['Alice', 'Bill']

print("")

bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)
# >>>
# ['Bill', 'Charlie']

print("")

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
# >>>
# ['Carrie']
print("")


bus3 = HauntedBus()
print(bus3.passengers)
# >>>
# ['Carrie']

print("")

bus3.pick('Dave')

print(bus2.passengers)
# >>>
# ['Carrie', 'Dave']

print("")

print(bus2.passengers is bus3.passengers)

# >>>True


# ❶ 目前没什么问题，bus1 没有出现异常。
# ❷ 一开始，bus2 是空的，因此把默认的空列表赋值给 self.passengers。
# ❸ bus3 一开始也是空的，因此还是赋值默认的列表。
# ❹ 但是默认列表不为空！
# ❺ 登上 bus3 的 Dave 出现在 bus2 中。
# ❻ 问题是，bus2.passengers 和 bus3.passengers 指代同一个列表。
# ❼ 但 bus1.passengers 是不同的列表。
# 问题在于，没有指定初始乘客的 HauntedBus 实例会共享同一个乘客列表。
# 这种问题很难发现。如示例 8-13 所示，实例化 HauntedBus 时，如果传入乘客，会按预
# 期运作。但是不为 HauntedBus 指定乘客的话，奇怪的事就发生了，这是因为
# self.passengers 变成了 passengers 参数默认值的别名。出现这个问题的根源是，默
# 认值在定义函数时计算（通常在加载模块时），因此默认值变成了函数对象的属性。因
# 此，如果默认值是可变对象，而且修改了它的值，那么后续的函数调用都会受到影响。





