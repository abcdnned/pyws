import os
import os.path

#input dist dir here
rootdir= 'D:\\gitrepo\\dcd\\dcd-parser\\src\\main\\java\\cn\\com\\netis\\dcd\\parser'

def check(p):
    i=open(p)
    start=0
    end=0
    mod=0
    lines=i.readlines()
    for idx,line in enumerate(lines):
        if 'public String toString()' in line:
            start=idx
            mod=1
        if mod==1:
            if '}' in line:
                end=idx
                mod=2
                
    i.close()
    
    if mod==2:
        out=open(p,'w')
        out.writelines(lines[:start-1])
        out.writelines(lines[end+1:])
        out.close()
        
    
            

def loop(root): 
    for parent,dirs,files in os.walk(root):
        for d in dirs:
            loop(d)
        for f in files:
            if f.endswith('Decoder.java') and not f.endswith('BaseDecoder.java'):
                check(os.path.join(parent,f))
            
loop(rootdir)
