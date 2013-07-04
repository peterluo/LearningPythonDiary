#! /usr/bin/env python
#coding=utf-8
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
x=Bag()
x.add(1)
x.addtwice(2)
print x.data

[1, 2, 2]