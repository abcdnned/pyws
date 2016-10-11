#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join

ws='C:\\Users\\tom.yang\\Desktop\\浙江省农信核心'

DEFINE_START='B'
i=open('d:\\20rep.csv')
lines=i.readlines()
defs=''
fd=True
index=0

def add_close():
    return '};\n'

def add_header(name):
    return 'HashMap<String,DecodeField'

def register(line):
    name=line[:8]
    return 'RSP_MAP.put("{}",{});'.format(name,name)

defs+=add_head()
for line in lines:
    if line.startswith(DEFINE_START):
        defs+=register(line)
defs+=add_close()

i.close()
o=open('d:\\reg.txt','w')
o.write(defs)
o.flush()
o.close()
