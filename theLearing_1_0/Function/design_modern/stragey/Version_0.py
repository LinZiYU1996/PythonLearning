# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/11 14:04'


from abc import ABC, abstractmethod

from collections import  namedtuple

Customer = namedtuple('Customer','name fidelity')

class LineItem:

    def __init__(self,product,quantity,price):
        self.product = product  # 产品
        self.quantity = quantity  # 数量
        self.price = price  # 价格

    """
    计算总价钱
    """
    def total(self):
        return self.price * self.quantity


class Order():

    def __init__(self,customer,cart,promotion = None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion # 积分

    def total(self):
        if not hasattr(self,'_total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<order total :{:.2f} due : {:.2f}'
        return fmt.format(self.total(),self.due())



# class Promotion(ABC):
#
#     @abstractmethod
#     def discount(self,order)：
#         pass



class FidelityPromotion(Promotion):

    """
    为积分1000以上用户提供5折优惠
    """

    def discount(self,order):
        return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0



class BulkItemPromotion(Promotion):

    """
    单个商品为20或者以上提供10%折扣
    """

    # def discount(self,order):
    #     discount = 0
    #     for item in order.cart:
    #         if item.quantity > = 20 :
    #             discount += item.total() * 0.1
    #     return discount









