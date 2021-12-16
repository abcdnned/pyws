#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join

ws='c:/Users/tom.yang/Desktop/jyrcb atmp/ubatmp_comm_req.xml'

i=open(ws)
lines=i.readlines()

defs=''

def add_header(name):
    return ' private static final Object[][][] {} = {{ \n'.format(name)

def add_close():
    return '};\n'

def addFieldDefine(index,length,name):
    return '{{ {{ {}, null, {}, Encoding.CHARSET }}, {{ "", ValueType.STRING, false, "{}" }} }},\n'.format(index,length,name)

defstart=False

def checkdefine(line):
    return  "PkgBody" in line 

def checkfield(line):
    return  "<Node name" in line

def checkend(line):
    return "</Node>" in line

def getin(s,start,end):
    s=line.find(start)
    e=line.find(end,s+len(start))
    return line[s+len(start):e]

index=0

for line in lines:
    if checkdefine(line):
        defstart=True
        defs+=add_header('BODY_DEF')
    elif defstart and checkfield(line):
        fn=getin(line,'<Node name="','"')
        l=getin(line,'len="','x"')
        defs+=addFieldDefine(index,l,fn)
        index+=1
    elif defstart and checkend(line):
        defstart=False
        defs+=add_close()

i.close()
o=open(join('d:/test/','jyrcbamtpdefine'),'w')
o.write(defs)
o.flush()
o.close()

