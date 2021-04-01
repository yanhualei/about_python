from django.contrib import admin
from django.utils.translation import gettext_lazy

from books.models import BookInfo


@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['b_id', 'b_name', 'image']
    # list_filter = ['b_id', 'b_name']  # 页面右面的过滤栏
    ordering = ['b_id']  # 排序
    search_fields = ['b_id', 'b_name']  # 搜索框可搜索的字段

    fieldsets = (  # 用户详情页的相关设置
        (None, {'fields':('b_id','b_name','image')}),  # 普通信息


    )
