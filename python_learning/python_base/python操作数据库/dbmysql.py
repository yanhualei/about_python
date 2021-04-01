#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

db = MySQLdb.connect(host="localhost",database='booksinfo',port=6379,
                     user='root',password='root',charset='utf8')
csr = db.cursor()  # 创建游标

# 查询
mysql = "select * from tb_booksinfo"
csr.execute(mysql)  # 执行sql语句
result = csr.fetchall()  # 获取所有执行结果
print(result)
db.close()  # 关闭链接

# 插入
# 更新
# 删除


