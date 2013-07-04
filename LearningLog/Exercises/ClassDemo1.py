#! /usr/bin/env python
#coding=utf-8
class classdemo:
    field='meimei:'
    def __init__(self,key,value):
        self.r=key
        self.y=value
    def PrintString(self,values):
        print self.field,values


u=classdemo(4,5)
print u.r,u.y
u.PrintString('is a female!')
u.field='peter:'
u.PrintString('is a male!')




    

        
        