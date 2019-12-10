from django.db import models

class BaseModel(models.Model):
    """为模型类补充字段"""

    # auto_now_add:第一次创建时自动设置当前时间
    # verbose_name = '创建时间':admin后台管理的字段名称
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    # auto_now:自动设置时间字段为当前时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True   # 说明是抽象模型类，用于继承使用，数据库迁移时不会创建BaseModle的表