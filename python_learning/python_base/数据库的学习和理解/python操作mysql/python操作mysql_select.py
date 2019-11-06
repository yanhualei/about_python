from pymysql import *


def main():
    # 创建connection连接
    conn = connect(host="localhost", port=3306, database="jing_dong", user="root", password="root", charset="utf8")
    # 获取cursor对象
    cs1 = conn.cursor()
    # execute操作数据库（增删改查）
    sql = 'select * from goods_cates'  # 数据库查询语句
    count = cs1.execute(sql)  # 返回的是查询到的行数
    # result = cs1.fetchall()  # 一次性全部读取
    # result = cs1.fetchmany(3) # 每次按需求读取
    for i in range(count):  # 对
        result = cs1.fetchone()  # 每次读取一行
        print(result)
    # 提交数据
    # conn.commit() #  当执行语句是查询语句时不用提交给数据库
    # 关闭cursor
    cs1.close()
    # 关闭数据库连接
    conn.close()


if __name__ == '__main__':
    main()