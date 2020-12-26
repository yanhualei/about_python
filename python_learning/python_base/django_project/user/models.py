from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):  # AbstractUser:Django框架预定义的User抽象类
    mobile = models.CharField(max_length=11,unique=True,verbose_name="手机号")

    class Meta:
        db_table = 'tb_users'  # 数据库里的表名
        verbose_name = '用户表'  # admin后台管理的表名
        verbose_name_plural = verbose_name  # 设置复数下的显示字段

