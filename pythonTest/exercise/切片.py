# -*- coding: utf-8 -*-
#取一个list的部分元素是非常常见的操作
#1. 前10个数；
#2. 3的倍数；
#3. 不大于50的5的倍数。
L = range(1, 101)

print L[:10]
print L[2::3]
print L[4:50:5]
print '----'
#利用倒序切片对 1 - 100 的数列取出：
#* 最后10个数；
#* 最后10个5的倍数。
print L[-10:]
print L[-51::5]

L = ['Adam', 'Lisa', 'Bart', 'Paul']
L[-2:]
#['Bart', 'Paul']
L[:-2]
#['Adam', 'Lisa']
L[-3:-1]
#['Lisa', 'Bart']
L[-4:-1:2]
#['Adam', 'Bart']

#对字符串的切片
'ABCDEFG'[:3]
#'ABC'
'ABCDEFG'[-3:]
#'EFG'
'ABCDEFG'[::2]
#'ACEG'
