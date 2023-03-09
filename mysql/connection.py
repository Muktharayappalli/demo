import pymysql

db = pymysql.connect(host="localhost",user="root",password="Mukthar@007",db="mydatabase")
obj=db.cursor()

obj.execute("SELECT VERSION()")

data = obj.fetchone()

print("your database version is:",data)

obj.execute("show tables")
output=obj.fetchall()
for i in output:
    print(i)

obj.execute("select * from persons")
out=obj.fetchall()
for j in out:
    print(j)
obj.execute("insert into persons values(9,'mmm',788898866,'vpp','ereje')")
obj.execute("select * from persons")
outp=obj.fetchall()
for i in outp:
    print(i)