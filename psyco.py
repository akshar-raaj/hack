import psycopg2
import sys
import pprint
import random
import string

#conn_string = "host='localhost' dbname='hack' user='hack' password='hack'"
conn_string = "host='localhost' dbname='hack'"
print "Connecting to database\n ->%s" % (conn_string)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print "Connected!\n"
cursor.execute("SELECT * FROM people")
records = cursor.fetchall()
#name = u'\u00e4'
#encoded_name = name.encode('8859')
#name = encoded_name
#cursor.execute("insert into names values ('%s')" % (name,))
#conn.commit()
for i in range(1000):
    name = ''.join([random.choice(string.ascii_lowercase) for i in range(6)])
    age = random.randint(20, 30)
    cursor.execute("insert into people(name, age) values ('%s', %d)" % (name, age))
conn.commit()