from pymysql import connect


"""
    此段程序主要练习python对数据库的增删改查，并未考虑程序的耦合度，属于初级程序
    1.完成python对数据库的简单的增删改查
    2.将where条件参数化，防止sql注入
    3.再次学习和理解面向对象以及__del__()函数
    4.加强了程序编辑的逻辑思维
    5.加强了变量和函数的命名习惯
"""
class JD(object):
    # 程序加载的时候，首先加载__init__()
    def __init__(self):
        self.conn = connect(host='localhost',port=3306, user='root', password='root', database='jing_dong',charset='utf8')
        self.cursor = self.conn.cursor()

    # 程序执行完之后，自动调用__del__()函数，从而关闭游标，关闭数据库连接，释放资源
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # 执行查询操作
    def get_goods_row(self):
        get_input = input("请输入产品id：")
        sql = """select * from goods where id =%s"""
        count = self.cursor.execute(sql,[get_input])
        for i in range(count):
            content_goods = self.cursor.fetchone()
            print(content_goods)
    # 执行插入操作
    def i_goods_cates(self):
        get_input = input("请输入产品类别")
        sql = """insert into goods_cates (name) values (%s)"""
        self.cursor.execute(sql,[get_input])
        self.conn.commit()
        print("-----------------------已经成功提交！-------------------------")
    # 执行修改操作
    def m_goods_cates(self):
        get_newname = input("请输入产品类别：")
        get_name = input("请输入新产品类别：")

        sql = """update goods_cates set name = %s where name = %s"""
        self.cursor.execute(sql, [get_newname,get_name])
        self.conn.commit()
        print("-----------------------已经成功提交！-------------------------")

    # 执行删除操作
    def d_goods_cates(self):
        get_input = input("请输入产品类别")
        sql = """delete from goods_cates where name = %s"""
        self.cursor.execute(sql, [get_input])
        self.conn.commit()
        print("-----------------------已经成功提交！-------------------------")
    def show_menu(self):
        print("0:退出系统")
        print("1:查询")
        print("2:修改")
        print("3:插入")
        print("4:删除")
        num = input("请选择您的操作:")
        return num
    def run(self):
        while True:
            num = self.show_menu()
            if num in ['1','2','3','4']:
                if num == '1':
                    self.get_goods_row()
                elif num == '2':
                    self.m_goods_cates()
                elif num == '3':
                    self.i_goods_cates()
                elif num == '4':
                    self.d_goods_cates()
            elif num == '0':
                print("欢迎再次使用！")
                break
            else :
                print("您选择的操作不存在...")

def main():
    jd = JD()
    jd.run()


if __name__ == '__main__':
    main()