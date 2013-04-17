#! /usr/bin/env python
#coding=utf-8
import os
print os.getcwd()
filenames = os.listdir(os.curdir)
for filename in filenames:
    print filename
    if filename != "ReNameForFiles2.py" and filename != "ReNameForFiles.py" and os.path.isfile(filename):
        t = filename.split('.')
        m=len(t)
        if t[m-2]=='PRC' and t[m-1]=='sql':
            #os.rename(filename,filename.replace('PRC.sql','PRC',1))
            os.rename(filename,filename.replace('PRC','rrrrr',1))
            
            
        
    
