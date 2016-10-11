def fetch(line):
    ex=False
    add=False
    for c in line:
        if c == '"':
            if ex:
                break
            tag=''
            add=True
            ex=True
        elif add:
            tag+=c
    if add:
        return tag
    return None
    


f=open('tag_name_fetcher_input')
first=True
result='<('
prefix=None
for line in f.readlines():
    if line.find('// buffer handler')!=-1:
        prefix='buf:'
    elif line.find('// core handler')!=-1:
        prefix='core:'
    else:
        tag=fetch(line)
        if tag!= None:
            if not first:
                result+='|'+tag
            else:
                result+=tag
                first=False
            if prefix != None:
                result+='|'+prefix+tag
result+=')'
f.close();
out=open('tag_name_fetcher_output','w+')
out.write(result)
out.close()

print result

