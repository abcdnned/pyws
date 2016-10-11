fl=True
index=0
i=open('qhdefine')
lines=i.readlines()
defs=''
pro=''

def get_protocols(line):
    global pro
    pro=line[6:12]
    return 'req_defs.put("{}", new Object[][][] {{\n'.format(pro)

def add_close():
    global fl
    if fl:
        fl=False
        return ''
    return '});\n'

def get_first_int(line):
    e=0
    endset=['A','N','F']
    for c in line:
        e+=1
        if c in endset:
            break
    return line[:e-1].strip()

def get_first_name(line):
    global index
    return pro+'F'+str(index+1)

def get_field_len(line):
    return line[line.find('(')+1:line.find(')')]

def get_field_name(line):
    s=line.find('ID')
    return line[s+4:line.find('"',s+4)]

def add_defineline(l,fn):
    global index
    index+=1
    return '{{ {{ {}, null, {}, Encoding.CHARSET }}, {{ "", ValueType.STRING, false, "{}" }} }},\n'.format(index,l,fn)


for line in lines:
    if 'define' in line:
        index=0
        defs+=add_close()
        defs+=get_protocols(line)
    elif 'Alphanumeric' in line or 'Numeric' in line or 'Filler' in line:
        l=get_first_int(line)
        fn=get_first_name(line)
        defs+=add_defineline(l,fn)
    elif '<FIELD' in line:
        l=get_field_len(line)
        fn=get_field_name(line)
        defs+=add_defineline(l,fn)

defs+=add_close()

i.close()
o=open('qhgen','w')
o.write(defs)
o.flush()
o.close()


