#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join

def getin(content,start,end):
    s=content.find(start)
    e=content.find(end,s+len(start))
    return content[s+len(start):e]

def getnumin(content):
    return ''.join(c for c in content if c.isdigit())

def hasdefname(line):
    return line[:4].isdigit() or line[:4].startswith('CK')

def checkdefine(line):
    return line[0]=='1' and not line[1].isdigit()

def checkfield(line):
    return line[0].isdigit()

def deffldmap(mapn):
    return 'static final Map<String,DecodeField[]> {} =new HashMap<String,DecodeField[]>();\n'.format(mapn)

def putfld(mapn,key,consn,fldn):
    return '{}.put("{}",{}.{});\n'.format(mapn,key,consn,fldn)

def fielddefine(index,l,fn,record=True,charset='Encoding.CHARSET'):
    if not record:
        return '{{ {{ {}, null, {}, {} }}, {{ "", null, false, "{}" }} }},\n'.format(index,l,charset,fn)
    return '{{ {{ {}, null, {}, {} }}, {{ "", ValueType.STRING, false, "{}" }} }},\n'.format(index,l,charset,fn)

def definehead(name):
    return ' private static final Object[][][] {} = {{ \n'.format(name)

def definecloser():
    return '};\n'

def staticfield(fieldname,defname):
    return 'static final DecodeField[] {} = new DecodeField[{}.length];\n'.format(fieldname,defname)

def fieldbuild(fieldname,defname):
    return 'BankFieldFactory.buildFields({},{});\n'.format(fieldname,defname)

def defineregmap(mapname,regname,fieldname):
    return '{}.put("{}", {})\n'.format(mapname,regname,fieldname)

def searchline(lines,s,pattern,limit):
    for i in range(limit):
        if pattern in lines[s+i]:
            return s+i
    return -1

def getname(line):
    return line[:4]

def gendeffilehead(pkg,deffn):
    return 'package cn.com.netis.dcd.parser.decoder.bank.{};\nimport cn.com.netis.dcd.parser.huygens.field.DecodeField;\nimport cn.com.netis.dcd.parser.huygens.field.Encoding;\nimport cn.com.netis.dcd.parser.huygens.field.bank.BankFieldFactory;\nimport cn.com.netis.dp.commons.lang.ValueType;\n\npublic class {} {{\n\n'.format(pkg,deffn)


def genmaphead(pkg,classn):
    return 'package cn.com.netis.dcd.parser.decoder.bank.{};\n\nimport java.util.HashMap;\nimport java.util.Map;\n\nimport cn.com.netis.dcd.parser.huygens.field.DecodeField;\n\npublic class {} {{\n'.format(pkg,classn)


i=open('c:/Users/tom.yang/Desktop/jyrcbwebbank/fields.csv')
lines=i.readlines()

rraflag=0

defs=''
fld=''
build=''
regs=''

deffn='WebbankFldDef'

firstflag=True
index=0
name=''

defined=0
limit=55
n=1

def defname(n,rraflag):
    rra='REQ_' if rraflag==0 else 'RESP_'
    n=rra+n
    defn='DEF_'+n
    fieldn='FIELD_'+n
    return (fieldn,defn)

def writedefs(defs,fld,build,f):
    o=open(f,'w')
    o.write(gendeffilehead('jyrcb',deffn+str(n)))
    o.write(defs)
    o.write(fld)
    o.write('static {\n')
    o.write(build)
    o.write('}\n')
    o.write('}\n')
    o.flush()
    o.close()

def writereg(n,regs,f,mapdef):
    o=open(f,'w')
    o.write(genmaphead('jyrcb','WebbankBodyFlds'))
    o.write(mapdef)
    o.write('static {\n')
    o.write(regs)
    o.write('}\n')
    o.write('}\n')
    o.flush()
    o.close()


outputws='c:/Users/tom.yang/Desktop/jyrcbwebbank/'
mapdefn='WebbankBodyFlds'


for ln,line in enumerate(lines):
    if hasdefname(line):
        name=getname(line)
        rraflag=0
    else:
        if checkdefine(line):
            if firstflag:
                firstflag=False
            else:
                defs+=definecloser()
            if defined>=limit:
                writedefs(defs,fld,build,'{}{}{}.java'.format(outputws,deffn,n))
                defs=''
                fld=''
                build=''
                defined=0
                n+=1
            index=0
            rra='REQ_' if rraflag==0 else 'RESP_'
            rraflag=(rraflag+1)%2
            defname='DEF_'+rra+name
            fieldname='FIELD_'+rra+name
            defs+=definehead(defname)
            fld+=staticfield(fieldname,defname)
            build+=fieldbuild(fieldname,defname)
            regs+=putfld('FIELD_MAP',name+rra[:-1].lower(),'{}{}'.format(deffn,n),fieldname)
            defined+=1
        if checkfield(line):
            itms=line.split(',')
            fn=itms[1]
            length=getnumin(itms[3])
            defs+=fielddefine(index,length,fn)
            index+=1

if defined>0:
    defs+=definecloser()
    writedefs(defs,fld,build,'{}{}{}.java'.format(outputws,deffn,n))

i.close()

writereg(n,regs,'{}{}.java'.format(outputws,mapdefn),deffldmap('FIELD_MAP'))

