#!/usr/bin/python
# -*- coding: UTF-8 -*-

class C(object):
    @staticmethod
    def f():
        print('我是静态类方法');


C.f();  # 静态方法无需实例化
cobj = C()
cobj.f()  # 也可以实例化后调用