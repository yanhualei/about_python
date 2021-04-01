from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy

from books.models import BookInfo
from .models import User

# Register your models here.

admin.site.site_header = '校园管理系统'
# admin.site.site_title = '郑州十一小学校园管理'
admin.site.index_title = '欢迎来到校园管理系统'

@admin.register(User)
class UserAdmin(UserAdmin):


    list_display = ['username', 'email', 'nick_name', 'gender', 'mobile']  # 要显示的字段
    list_filter = ['gender']  # 页面右面的过滤栏
    ordering = ['username', 'nick_name']  # 排序
    search_fields = ['username', 'email', 'mobile']  # 搜索框可搜索的字段

    fieldsets = (  # 用户详情页的相关设置
        (gettext_lazy('Important dates'), {'fields': ('last_login', 'date_joined')}),  # 重要信息
        (None,{'fields':('username','password','first_name','last_name','email')}),  # 普通信息

        (gettext_lazy('Personal info'),{'fields':('nick_name','gender',
                                                     'mobile',)}),  # 个人信息

        (gettext_lazy('Permissions'), {'fields': ('is_superuser','is_staff','is_active',
                                                  'groups', 'user_permissions')}),  # 权限


    )


