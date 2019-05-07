import mysql.connector

mydb = mysql.connector.connect(
  host="***",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="***" ,  # 数据库密码
  database="rundb"
)
 
mycursor = mydb.cursor()

# mycursor.execute('CREATE DATABASE rundb')

#创建数据表
mycursor.execute('CREATE TABLE sites (name VARCHAR(255),url VARCHAR(255))')

# 插入数据 mycursor.execute(sql, val) 批量插入 executemany()
slq = "INSERT INTO sites (name,url) VALUES (%s,%s)"
val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]

mycursor.executemany(slq, val)



# 查询数据 SELECT 

mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)