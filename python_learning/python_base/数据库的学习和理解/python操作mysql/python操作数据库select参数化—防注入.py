from pymysql import *
def main():

    # 创建connection连接
    conn = connect(host="localhost", port=3306, database="jing_dong", user="root", password="root", charset="utf8")
    # 获取cursor对象
    cs1 = conn.cursor()
    # execute操作数据库（增删改查）
    find_name = input("请输入产品类型id：")
    params = [find_name]
    sql = 'select * from goods where cate_id = %s'  # 数据库查询语句
    count = cs1.execute(sql, params)  # 返回的是查询到的行数
    result = cs1.fetchall()  # 一次性全部读取
    print(result)
    # 提交数据
    # conn.commit() # 注意：python程序操作mysql时，时在内存中的操作，如果没有事务的提交，是不会保存到数据库物理表的。
    # 关闭cursor
    cs1.close()
    # 关闭数据库连接
    conn.close()


if __name__ == '__main__':
    main()