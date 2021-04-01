import hashlib
import json
import time
from audioop import reverse

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core import signing
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from users import models
from users.models import User

def index(request):  # request:固定参数，接受请求
    context = {}
    context['datas'] = "Hello,Django!"
    return render(request,'index.html',context)  # 将数据渲染到模板的datas中


@csrf_exempt  # 取消当前函数防跨站请求伪造功能
def test_jsonresponse(request):
    datas = {"username":"","password":""}
    datas["username"] = request.GET.get('username')  # 获取post中表单内容
    datas["password"] = request.GET.get("password")
    print(datas)
    return JsonResponse(datas)  # 直接返回json数据


def register(request):
    """
    auth注册
    :param request:
    :return:
    """
    username = request.GET.get('username')
    password = request.GET.get('password')
    mobile = request.GET.get('mobile')
    if username == "" or password == "":
        return JsonResponse({'message': 'username or passowrd is null !!!'})

    result = User.objects.filter(username=username)
    if result:
        return JsonResponse({'message': 'username is already exists !!!'})

    try:
        User.objects.create_user(username=username, password=password,mobile=mobile)

    except ValidationError as e:
        error = "####create data worng#############"
        return JsonResponse({'ststus': 10024, 'message': error})
    return JsonResponse({'username': username, 'message': 'regist ok!'})


def login(request):
    """
    auth登录
    :param request:
    :return:
    """
    # print(request.method)
    if request.method == 'POST':
        # print(request.method,request.POST,request.body)
        username = request.POST["username"]
        password = request.POST["password"]
        # print(username,password)
        user = auth.authenticate(username=username, password=password)
        if user:
            print('ok')
            auth.login(request, user)
            return redirect('/after_login/')  # 将数据传递到目标视图函数after_login,相当于我们向after_longin发起了一个request请求，并且携带user相关数据
        else:
            return render(request, 'login.html', {'errormsg': '用户名或密码错'})

def modify_pwd(request):
    """
    auth修改密码
    :param request:
    :return:
    """
    username = request.POST["username"]
    old_password = request.POST["old_password"]
    user = auth.authenticate(username=username, password=old_password)
    if user:
        new_password = request.POST["new_password"]
        user.set_password(new_password)
        user.save()
        print("update ok")
        return render(request,"index.html", {'datas':'update success!'})
    else:
        return redirect('/index/', {'datas':'update failed!'})


@login_required
def after_longin(request):
    return render(request, 'index.html', {'message': request.user.username,"datas":request.user.username})


def logout(request):
    auth.logout(request)

    return redirect('/after_logout/')


def after_logout(request):
    res = {}
    res["code"] = 10000
    res['data'] = "logout success!"
    # HttpResponse生成格式为HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
    # content_type:见云笔记content_type详情页
    return HttpResponse(json.dumps(res),content_type='application/json',status=200)

