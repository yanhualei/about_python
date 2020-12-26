from django.db import models

# Create your models here.
from django.utils import timezone


class Author(models.Model):
    author_id = models.CharField(max_length=11,primary_key=True,unique=True,verbose_name="编号")
    author_name = models.CharField(max_length=20,verbose_name="姓名")
    phone = models.CharField(max_length=11,unique=True,verbose_name="手机号")
    created_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        db_table = "tb_authors"
        verbose_name = "作者表"
        verbose_name_plural = verbose_name


class Book(models.Model):
    book_id = models.CharField(max_length=11,primary_key=True,unique=True,verbose_name="书籍编号")
    book_name = models.CharField(max_length=20,verbose_name="书籍名称")
    author = models.ForeignKey(Author,related_name="book_author",on_delete=models.CASCADE,verbose_name="作者姓名")

    class Meta:
        db_table = "tb_books"
        verbose_name = "书籍表"
        verbose_name_plural = verbose_name


