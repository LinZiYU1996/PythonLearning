# -*- coding: utf-8 -*-
# @Time  : 2019/11/17 20:04
# @Author : Mr.Lin


"""

寻找序列交集
"""

def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return  res

s1 = "SPAM"

s2 = "SCAM"

print(intersect(s1,s2))
# >>>
# ['S', 'A', 'M']

# 列表解析
res = (x for x in s1 if x in s2)
print(res)
















