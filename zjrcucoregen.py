#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join

#config
deff='c:/Users/tom.yang/Desktop/scrcuepos/def.txt'
rra=True

def checkdefine(line):
    pass

def parse_define_name(line):
    pass

def isFieldLine(line):
    return line[0].isdigit()

def getFieldName(line):
    pass

def getFieldLength(line):
    pass

#system methods
def getin(content,start,end):
    s=content.find(start)
    e=content.find(end,s+len(start))
    return content[s+len(start):e]

def getnumin(content):
    return ''.join(c for c in content if c.isdigit())

def fielddefine(index,l,fn):
    return '{{ {{ {}, null, {}, Encoding.CHARSET }}, {{ "", ValueType.STRING, true, "{}" }} }},\n'.format(index,l,fn)

def add_close():
    return '};\n'

def add_header(name):
    return ' private static final Object[][][] {} = {{ \n'.format(name)

def staticfield(fieldname,defname):
    return 'static final DecodeField[] {} = new DecodeField[{}.length];\n'.format(fieldname,defname)

def fieldbuild(fieldname,defname):
    return 'BankFieldFactory.buildFields({},{});\n'.format(fieldname,defname)

#logic
i=open(deff)
lines=i.readlines()
defs=''
fd=True
index=0
blds=''
fld=''
req=True

for line in lines:
    if checkDefine(line):
        if not fd:
            defs+=add_close()
        defn=parse_define_name(line)
        if rra :
            defn = defn + '_REQ' if req else defn + '_RESP'
            req = not req
        defs+=add_header(defn+'_DEF')
        fld+=staticfield(defn+'_FIELD',defn+'_DEF')
        blds+=fieldbuild(defn+'_FIELD',defn+'_DEF')
        index=0
        fd=False
    elif isFieldLine(line):
        fn=getFieldName(line)
        len=getFieldLength(line)
        defs+=fielddefine(index,length,fn)
        index+=1
defs+=add_close()

i.close()
o=open('d:\\rspleft.txt','w')
o.write(defs)
o.write(fld)
o.write('static {\n')
o.write(blds)
o.write('}\n')
o.flush()
o.close()
