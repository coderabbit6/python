import pymysql
con = pymysql.connect(host = '127.0.0.1',port = 3306,user = "test",passwd = "12345678",db = 'test1')
cur = con.cursor()
# cur.execute("SELECT * FROM students")
# cur.execute('CREATE TABLE teachers (id int not null auto_increment primary key,name varchar(20),age int)')
# cur.execute("INSERT INTO teachers (name,age) VALUES ('changyan',30)")
# cur.execute("INSERT INTO teachers (name,age) VALUES ('liwei',30)")
# cur.execute("INSERT INTO teachers (name,age) VALUES ('weidong',30)")
# cur.executemany("INSERT INTO teachers (name,age) VALUES(%s,%s)",[('王鑫炎',20),('贾凡',20)])
# cur.execute("DELETE FROM teachers WHERE name = '贾凡'")
# cur.execute("DELETE  FROM teachers ")
# cur.execute('CREATE TABLE SHU (id int not null auto_increment primary key ,name varchar(20),age int)')
cur.execute('DELETE FROM SHU')
list = [(1,'刘备',40),(2,'关羽',35),(3,'张飞',33)]
insert_commend = 'INSERT INTO SHU (id,name,age) VALUES(%s,%s,%s)'
cur.executemany(insert_commend,list)
cur.execute("SELECT id,name,age FROM SHU")
con.commit()
# cur.execute("SELECT * FROM teachers")
for i in cur.fetchall() :
	print(i)
cur.close()
con.close()