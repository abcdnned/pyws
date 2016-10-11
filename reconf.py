import os
import os.path

rootdir='D:\\gitrepo\\dp-benchmarks\\acceptance'
pf='acceptance/'

def reconf(d,f):
    try:
        i=open(f)
        lines=i.readlines()
        nl=[]
        for line in lines:
            if 'dp-benchmarks/' in line:
                s=line.find('dp-benchmarks/')+14
                e=line.find('/',s)
                print line[s:e]
                line=line.replace(line[s:e],pf+d)
            nl.append(line)
        i.close()
        i=open(f,'w')
        i.writelines(nl)
        i.flush()
        i.close()
    except:
        pass

for root,dirs,files in os.walk(rootdir):
    for d in dirs:
        reconf(d,os.path.join(root,d,'conf.json'))
        reconf(d,os.path.join(root,d,'templates','file.vm'))
        reconf(d,os.path.join(root,d,'templates','file.xml'))
