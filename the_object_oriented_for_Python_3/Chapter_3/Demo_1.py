# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/19 15:58'


"""
基本继承
"""

class Contact:
    '被所有类实例共享'
    all_contacts = []

    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):

    '添加子类自己的方法'
    def order(self,order):
        print("if this were a real system we would send"
              "{} order to {}".format(order,self.name))


c = Contact("some body","somebody ner")
s = Supplier("super","super.net")

print(c.name,c.email,s.name,s.email)
# >>>
# some body somebody ner super super.net

print(c.all_contacts)
# >>>
# [<__main__.Contact object at 0x033A0910>, <__main__.Supplier object at 0x033A08D0>]

s.order("ANANA")

# >>>
# if this were a real system we would sendANANA order to super
