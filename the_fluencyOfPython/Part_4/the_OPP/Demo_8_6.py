# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/17 16:42'

import weakref

class Cheese:

    def __init__(self,kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()

catalog = [
    Cheese('a'),
    Cheese('b'),
    Cheese('c')

]

for cheese in catalog:
    stock[cheese.kind] = cheese

sorted(stock.keys())
print(sorted(stock.keys())
)
# >>>
# ['a', 'b', 'c']

# print(stock.keys())

del  catalog
print("")
print(sorted(stock.keys())
)
# >>>
# ['c']

