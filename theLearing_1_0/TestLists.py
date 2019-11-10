"""
列表的使用
"""

a_List = [1,'2',546,"asas"]

print(a_List)


"""
列表切片
"""

# 右边索引不包含在内
print(a_List[0:3])


# 起点从 0 开始  左边缺省
print(a_List[:3])


# 右边缺省
print(a_List[3:])

# 两边缺省
print(a_List[:])

"""
列表添加元素
"""

b_List = []

# 第一种形式
b_List = b_List + [1,222,33]

print(b_List)

# 第二种形式
b_List.append(True)

print(b_List)

# 第三种形式
b_List.extend(['a','aaa','aaaaa'])

print(b_List)

# 第三种形式
# b_List.insert('h','hhh','hhhhh')

# print(b_List)


"""
在列表中索引值
"""

c_List = [1,2,3,4,5,6,7,8,9,'a']

print(c_List.count('a'))

print(1 in c_List)

print(c_List.index(1))


"""
从列表中删除元素
"""

d_List = [1,2,3,4,5,6,7,8,9]


# 通过索引来删除元素
del d_List[1]

print(d_List)

# 直接删除指定值
d_List.remove(1)

print(d_List)


# 特别  通过pop删除

print(d_List.pop())