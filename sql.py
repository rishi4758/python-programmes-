import sqlite3
c=sqlite3.connect("thpolkj2.db")
s=c.cursor()
s.execute("create table emp5(name text,address text,age real)")
s.execute("insert into emp5 values('rishav','lpu',20)")
s.execute("insert into emp5 values('adarsh','pune',000)")
s.execute("select * from emp5")
l1=[(4,'we',23),(25,'ty',9),(0,'oi',98)]
s.executemany('insert into emp5 values(?,?,?)',l1)
print(s.fetchmany(3))
c.commit()
c.close()
          
