#!/usr/bin/env python
# -*- coding: utf-8 -*-

#print 'hello, world';
#print 100+200;

# def fn(x,y):
# 	return x * 10 + y

#print reduce(fn, [1, 3, 5, 7, 9])
#################################################################
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。

# def fn1(s):
# 	return s[0].upper()+s[1:].lower()

# print map(fn1,['adam', 'LISA', 'barT'])
#################################################################
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。

# print 45678+0x12fd2
# print  'Learn Python in imooc.'
# print 100<99
# print 0xff==255
# def prod():


# abc = [1,2,3,4,5,6,7,8,9]

# reduce(prod,)

#######################################
#切片start
#######################################
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#1
# print [L[0], L[1], L[2]]

#2
# r = []
# n = 3
# for i in range(n):
# 	r.append(L[i])

# print r

#3 从0-3，不包括3
#print L[0:3]
#4
# print L[-2:]
# print L[-2:-1]

#5
# L = range(100)
# print L[:10]
# print L[-10:]
# print L[10:20]
# print L[:10:2]
# print L[::5]

#6tuple
# print 'ABCDEFG'[:3]
# print 'ABCDEFG'[::2]

#######################################
#切片end
#######################################

