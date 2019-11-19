# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/19 16:10'


"""
扩展内置类
"""

'扩展了list类'
class ContactList(list):


    def search(self,name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts


class Contact():

    all_contacts = ContactList()

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)



c1 = Contact("John A","123.com")

c2 = Contact("Mike B","456.com")

c3 = Contact("KIL,LL","9090.com")

print(c.name for c in Contact.all_contacts.search("John A"))

# >>>
# <generator object <genexpr> at 0x01745FB0>











