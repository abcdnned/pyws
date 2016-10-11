import os
import os.path

#input dist dir here
rootdir= 'D:\\eclipsews\\workspace\\3.9'
count=0

def loop(root): 
    for parent,dirs,files in os.walk(root):
        for d in dirs:
            loop(d)
        for f in files:
            global count
            count=count+1
            print f

loop(rootdir)
print 'total file number : '+str(count)




