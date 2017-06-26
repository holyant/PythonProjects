# -*- coding: utf-8 -*-
import math
def is_sqr(x):
    return math.sqrt(x)%1==0
    #r = int(math.sqrt(x))
    #return r*r==x
print filter(is_sqr,range(1, 100))
