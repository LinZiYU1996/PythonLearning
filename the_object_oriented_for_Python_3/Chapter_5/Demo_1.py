# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/20 16:51'


"""
求多边形的周长
"""

import math

'单纯使用函数解决'
def diance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1]) ** 2 )

def permiter(polygon):
    per = 0

    points = polygon + [polygon[0]]

    for i in range(len(polygon)):
        per += diance(points[i],points[i+1])

    return per



square = [(1,1),(1,2),(2,2),(2,1)]
print(permiter(square))
# >>>
# 4.0


'使用OOP'

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)



class Polygon:

    def __init__(self):

        self.vecs = []

    def add_points(self,point):
        self.vecs.append((point))


    def permiter(self):

        per = 0

        points = self.vecs + [self.vecs[0]]

        for i in range(len(self.vecs)):

            per += points[i].distance(points[i+1])

        return per


square_1 = Polygon()

square_1.add_points((1,1))
square_1.add_points((1,2))
square_1.add_points((2,2))
square_1.add_points((2,1))

print(square_1.permiter())




