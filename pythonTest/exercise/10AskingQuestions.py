#!/usr/bin/env python
# -*- coding: UTF-8 -*-
print "How old are you?",  #有逗号，结果才在一行里
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

"""
How old are you? 23
How tall are you? 154
How much do you weigh? 65
So, you're '23' old, '154' tall and '65' heavy.

What's the difference between input() and raw_input()?
The input() function will try to convert things you enter 
as if they were Python code, but it has security problems so you should avoid it.
"""