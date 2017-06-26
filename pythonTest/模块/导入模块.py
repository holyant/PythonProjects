import math, logging
#如果我们只希望导入用到的os.path模块的某几个函数，而不是所有函数，可以用下面的语句
from os.path import isdir,isfile
#如果方法重名,可以起别名
from logging import log as logger

print isdir(r'/Users/holyant/Documents/PythonProjects/pythonTest')
print isfile(r'/Users/holyant/Documents/PythonProjects/pythonTest/hello.py')
