import sqlite3
conn=sqlite3.connect('GUI.db')
c=conn.cursor()
#create table
c.execute("CREATE TABLE abc(name text,mobile text,age text,PINCODE text,Password text)")
#insert a row of data

#save (commit) the changes
#conn.commit()
#we can also close the connection if we are done with it
#just be sure any changes have been committed
conn.close()
