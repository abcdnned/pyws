#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join

def getin(content,start,end):
    s=content.find(start)
    e=content.find(end,s+len(start))
    return content[s+len(start):e]

def checkdefine(line):
    return '_RRA' in line

def checkfield(line):
    return '<field' in line

def fielddefine(index,l,fn,record=True,charset='Encoding.CHARSET'):
    if not record:
        return '{{ {{ {}, null, {}, {} }}, {{ "", null, false, "{}" }} }},\n'.format(index,l,charset,fn)
    return '{{ {{ {}, null, {}, {} }}, {{ "", ValueType.STRING, false, "{}" }} }},\n'.format(index,l,charset,fn)

def definehead(name):
    return ' private static final Object[][][] {} = {{ \n'.format(name)

def definecloser():
    return '};\n'

def staticfield(fieldname,defname):
    return 'private static final DecodeField[] {} = new DecodeField[{}.length];\n'.format(fieldname,defname)

def fieldbuild(fieldname,defname):
    return 'BankFieldFactory.buildFields({},{});\n'.format(fieldname,defname)

def defineregmap(mapname,regname,fieldname):
    return '{}.put("{}", {})\n'.format(mapname,regname,fieldname)

def searchline(lines,s,pattern,limit):
    for i in range(limit):
        if pattern in lines[s+i]:
            return s+i
    return -1

i=open('d:/gitrepo/dcd/dcd-parser/src/main/resources/cn/com/netis/dcd/parser/galilei/xdlsrc/bank/scrcu/core.xml')
lines=i.readlines()

defs=''
fld=''
build=''

firstflag=True
index=0

for ln,line in enumerate(lines):
    if checkdefine(line):
        if firstflag:
            firstflag=False
        else:
            defs+=definecloser()
        index=0
        name=getin(line,'\'','\'').upper()
        defname='DEF_'+name
        fieldname='FIELD_'+name
        defs+=definehead(defname)
        fld+=staticfield(fieldname,defname)
        build+=fieldbuild(fieldname,defname)
    elif checkfield(line):
        lenthline=searchline(lines,ln,'<L>',5)
        vline=searchline(lines,ln,'<V>',5)
        l=getin(lines[lenthline],'<L>','</L>')
        fn=getin(line,'"','"')
        if not vline==-1:
            defs+=fielddefine(index,l,fn,False,"Encoding.EBCDIC")
        else:
            defs+=fielddefine(index,l,fn,True,"Encoding.EBCDIC")
        index+=1

defs+=definecloser()
        

i.close()
o=open('d:/test/dcdgendef/scrcu_core_define','w')
o.write(defs)
o.write(fld)
o.write(build)
o.flush()
o.close()

