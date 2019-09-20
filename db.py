#!/usr/bin/python3

import pymysql

# 打开数据库连接
#db = pymysql.connect("192.168.10.15","root","Tiger_sun123")
db = pymysql.connect("120.92.76.197","root","flj123456")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("use exam_admin_db;")
cursor.execute("show tables;")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
s = []
for i in data:
    for j in i:

        s.append(j)
#print(s)
t=''
for i in s:
    t+='ALTER TABLE %s CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;\n' %(i)
# ALTER TABLE logtest CONVERT TO CHARACTERSET utf8 COLLATE utf8_general_ci;
f = open('exam_admin_db.txt','w')
f.write(t)
# print ("Databases : %s " % data)

# 关闭数据库连接
db.close()
