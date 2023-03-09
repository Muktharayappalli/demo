import pymysql

db = pymysql.connect(host="localhost",user="root",password="Mukthar@007",db="mydatabase")
obj=db.cursor()

#obj.execute("create table collag(id int,name varchar(30))")
obj.execute("insert into collag values(1,'sha'),(2,'gg'),(3,'ggf')")
obj.execute("select * from collag")
outp=obj.fetchall()
for i in outp:
      print(i)
