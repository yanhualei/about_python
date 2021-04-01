#!/usr/bin/python
# -*- coding: UTF-8 -*-


class B(object):

    def f(cls):
        print('{}:我是类方法'.format(cls))


class C(object):

    @staticmethod
    def f():  # 本质上静态类方法与此类没什么关系，需要类对象和实例对象共同调用时可定义静态类方法
        print('我是静态类方法')


C.f()  # 类对象可调用

cobj = C()
cobj.f()  # 实例对象也可调用

B.f("hellow")  # 类对象调用类方法