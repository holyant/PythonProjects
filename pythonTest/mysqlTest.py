#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='fanghao',db='my_db',port=3306)
    cur=conn.cursor()
    cur.execute('SELECT VERSION()')
    data = cur.fetchone()
    print "Database version : %s " % data
    cur.close()
    conn.close()
    print "hello"
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])