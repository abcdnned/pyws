#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join

def getin(content,start,end):
    s=content.find(start)
    e=content.find(end,s+len(start))
    if s==-1 or e==-1:
        return ''
    return content[s+len(start):e]

def checkdefine(line):
    return '<pkg_struct>' in line

def checkfield(line):
    return '<var_id>' in line

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
        if s+i<len(lines) and pattern in lines[s+i]:
            return s+i
    return -1

def getdefine(infile,name):
    i=open(infile)
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
            defname='DEF_'+name
            fieldname='FIELD_'+name
            defs+=definehead(defname)
            fld+=staticfield(fieldname,defname)
            build+=fieldbuild(fieldname,defname)

        elif checkfield(line):
            fn=getin(line,'<var_id>','</var_id>')
            if len(fn)>0:
                lenthline=searchline(lines,ln,'<fld_len>',10)
                l=getin(lines[lenthline],'<fld_len>','</fld_len>')
                if not l=='0':
                    defs+=fielddefine(index,l,fn,True,'Encoding.EBCDIC')
                    index+=1

    defs+=definecloser()
    i.close()
    return (defs,fld,build)

def getTransCode(content):
    if content.startswith('CH'):
        return content[:6]
    return content[:4]

def writedfs(ws,contents):
    out=open(ws+'scrcu_core_fields'+str(n),'w')
    out.write(contents[0])
    out.write(contents[1])
    out.write('static {\n')
    out.write(contents[2])
    out.write('}\n')
    out.flush()
    out.close()

n=1
defined=0

top50=open('c:/Users/tom.yang/Desktop/scrcucore/top50.csv')
lines=top50.readlines()

transcodes=[]
for line in lines:
    if line[0].isdigit():
        cells=line.split(',')
        transcodes.append(getTransCode(cells[1]))

top50.close()

transdic=open('c:/Users/tom.yang/Desktop/scrcucore/list.csv')
lines=transdic.readlines() 
mp={}

for line in lines:
    if line[0].isdigit():
        cells=line.split(',')
        mp[cells[1]]=(cells[4],cells[3])

transdic.close()

ws='c:/Users/tom.yang/Desktop/scrcucore/channel/'
output='d:/test/dcdgendef/'

dfs=''
flds=''
blds=''

reg=''


for tc in transcodes:
    if mp.has_key(tc):
        for idx,rra in enumerate(('REQ_','RESP_')):
            defs=getdefine(ws+mp[tc][idx]+'.xml',rra+tc)
            reg+='TRAN_FLDS.put("{}",{}.FIELD_{}{});\n'.format(rra+tc,'Core'+str(n),rra,tc)
            defined+=1
            dfs+=defs[0]
            flds+=defs[1]
            blds+=defs[2]
            if defined>25:
                writedfs(output,(dfs,flds,blds))
                n+=1
                defined=0
                dfs=''
                flds=''
                blds=''

if defined>0:
    writedfs(output,(dfs,flds,blds))

out=open(output+'register','w')
out.write(reg)
out.flush()
out.close()



    
