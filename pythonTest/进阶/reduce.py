# -*- coding: utf-8 -*-
#Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：

def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])
