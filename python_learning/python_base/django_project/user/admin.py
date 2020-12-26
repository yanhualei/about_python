from django.contrib import admin

# Register your models here.
from user.models import User

VERBOSE_APP_NAME='用户'

admin.site.register(User)