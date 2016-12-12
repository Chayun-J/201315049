# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import MySQLdb
import MySQLdb.cursors
import sys

filename = sys.argv[1]

try:
	conn = MySQLdb.connect(user='root', passwd='secret', db='prac', host='localhost', charset='utf8', use_unicode=True)
	cursor = conn.cursor()
except MySQLdb.Error, e:
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

f = open(filename, 'r')		
contents = f.readlines()[1:]
f.close()
for content in contents:
	cursor.execute("select * from prac where link = %s and articleSubject = %s and numberOfKeyword = %s", (content[0].encode('utf-8'), content[1].encode('utf-8'), content[2].encode('utf-8')))
	result = cursor.fetchone()

	if result:
		print "data already exist"
	else:
		try:
			cursor.execute('insert into prac(link, articleSubject, numberOfKeyword) values (%s, %s, %s)', (content[0].encode('utf-8'), content[1].encode('utf-8'), content[2].encode('utf-8')))
			conn.commit()
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])