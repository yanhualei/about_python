from pymysql import *


def main():
    # 创建connection连接
    conn = connect(host="localhost", port=3306, database="jing_dong",
                   user="root", password="root", charset="utf8")
    # 获取cursor对象
    cs1 = conn.cursor()
    # execute操作数据库（增删改查）
    sql = 'insert into goods_cates (name) values ("ooo")'  # 插入数据
    # sql = 'update goods_cates set name ="rrr" where name = "qqq"'  # 更新数据
    # sql = 'delete from goods_cates where name = "www"'             # 删除数据
    count = cs1.execute(sql)  # 返回的是查询到的行数
    print(count)
    # 操作完毕，事务提交
    conn.commit()  # python操作数据库是在内存中进行，
    # python的增删改如果不进行事务提交，那么更改的数据将不会影响数据库物理表
    # 关闭cursor
    cs1.close()
    # 关闭连接
    conn.close()


if __name__ == '__main__':
    main()