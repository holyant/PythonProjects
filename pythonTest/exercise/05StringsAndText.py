#!/usr/bin/env python
# -*- coding: UTF-8 -*-
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x #这里没有引号，但显示出来跟下面一样。
print "I also said: '%s'." % y  #这里有引号

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 
# 字符串连接

#What's the point of %s and %d when you can just use %r?
#The %r is best for debugging, and the other formats are for 
#actually displaying variables to users.