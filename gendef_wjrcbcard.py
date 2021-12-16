#!/usr/bin/env python
# -*- coding: utf-8 -*-

f=open('c:/Users/tom.yang/Desktop/wjrcb/def.txt')
lines=f.readlines()

defs=''
arr=[]
dn=''

def getnumin(content):
    return ''.join(c for c in content if c.isdigit())

def gendef(transid,arr):
    r='TRANSMAP.put("{}", new int[]{{'.format(transid)
    for i in range(0,len(arr)-1):
        r+='{},'.format(arr[i])
    r+='{} }});\n'.format(arr[-1])
    return r

for line in lines:
    if line[0]=='f':
        if len(arr)>0:
            defs+=gendef(dn,arr)
            arr=[]
        dn=line[1:7]
    else:
        its=line.split(',')
        fid=getnumin(its[0])
        arr.append(fid)
defs+=gendef(dn,arr)


f.close()
with open('c:/Users/tom.yang/Desktop/wjrcb/gen.txt','w') as output:
    output.writelines(defs)
    output.flush()
    output.close()
