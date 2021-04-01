import time

from django.db import models




#图书管理器
# class BookInfoManager(models.Manager):
#     def all(self):
#         #默认查询未删除的图书信息
#         #调用父类的成员语法为：super().方法名
#         return super().filter(is_delete=False)
#
#     # 创建书籍
#     def create_book(self, title, pub_date):
#         # 创建模型类对象self.model可以获得模型类
#         book = self.model()
#         book.btitle = title
#         book.bpub_date = pub_date
#         book.bread = 0
#         book.bcommet = 0
#         book.is_delete = False
#         # 将数据插入进数据表
#         book.save()
#         return book


# Create your models here.
class BookInfo(models.Model):

    # books = BookInfoManager()
    random_book_default_name = str(int(time.time()))

    image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)
    b_name = models.CharField(max_length=30,verbose_name="图书名",default="book_"+random_book_default_name,unique=True)
    b_id = models.IntegerField(default=int(time.time()),verbose_name="图书编号",primary_key=True)

    class Meta:
        db_table = 'books_bookinfo'  # 数据库迁移设置的表名,可省略,django自动生成表名:类名第一个单词复数形式_类名
        verbose_name = '书籍表'  # admin管理页面显示的表名
        verbose_name_plural = verbose_name  # 设置复数下的显示字段
        app_label = "books"

    def __str__(self):
        return  self.b_name

