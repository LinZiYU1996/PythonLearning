
"""
集合的使用
"""

a_Set = {1,2,3}

print(type(a_Set))

"""
以列表为基础创建集合
"""

a_List = [1,2,3,4,5,6,7]

b_Set = set(a_List)

print(b_Set)


# 修改集合

c_Set = {1,2,3,4,5,6,7,8,9}

c_Set.add(11111)

print(c_Set)

print(len(c_Set))

c_Set.update({'a','v'})

print(c_Set)