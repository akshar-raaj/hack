import psycopg2
import sys
import pprint

conn_string = "host='localhost' dbname='hack' user='hack' password='hack'"
print "Connecting to database\n ->%s" % (conn_string)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print "Connected!\n"
cursor.execute("SELECT * FROM names")
records = cursor.fetchall()
#name = u'shabda'
name = u'\u00e4'
encoded_name = name.encode('8859')
name = encoded_name
cursor.execute("insert into names values ('%s')" % (name,))
conn.commit()
pprint.pprint(records)