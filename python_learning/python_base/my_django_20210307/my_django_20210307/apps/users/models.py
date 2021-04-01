from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):  # 在django自带user模型基础上扩展

    gender_choise = [
        (1,"male"),
        (0,"famale")
    ]

    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    nick_name = models.CharField(max_length=50,null=True,verbose_name="昵称")
    gender = models.SmallIntegerField(choices=gender_choise,default=1,verbose_name="性别")

    class Mete:
        db_table = 'tb_users'
        verbose_name = '用户'
        # 设置复数下的显示字段
        verbose_name_plural = verbose_name



