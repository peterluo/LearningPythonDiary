#! /usr/bin/env python
#coding=utf-8
class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'
x = MyClass()
x.f()
xf = x.f
while True:
    print xf()
