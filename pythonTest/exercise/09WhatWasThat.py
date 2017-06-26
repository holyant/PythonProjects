#!/usr/bin/env python
# -*- coding: UTF-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

a tiny piece of fun code to try out:
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

#When I use a %r format none of the escape sequences work.
#That's because %r is printing out the raw representation of what you typed, 
#which is going to include the original escape sequences. Use %s instead. 
#Always remember this: %r is for debugging, %s is for displaying.