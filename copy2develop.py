import sys
from shutil import copyfile
from os.path import join
import os

ws='c:/Users/tom.yang/Desktop/'
dcddir='D:/gitrepo/dcd/dcd-parser/src/main/java/'
type='bank'

def getNewPath(pkgline,surfix):
    npkg=pkgline.replace(type,type+'.'+surfix)
    pkg=npkg[8:-2]
    np=pkg.replace('.','/')
    return (npkg,join(dcddir,np))


def main():
    if sys.argv>2:
        dtdir=sys.argv[1]
        surfix=sys.argv[2]
        root=join(ws,dtdir)
        for parent,dirs,files in os.walk(root):
            for f in files:
                if (not f.endswith('Test.java') and f.endswith('.java')) or f.endswith('Decoder.java'):
                    dcdsrc=open(join(parent,f))
                    content=dcdsrc.readlines()
                    dcdsrc.close()
                    (newpkg,newpath)=getNewPath(content[0],surfix)
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    newsrc=open(join(dcddir,newpath,f),'w')
                    newsrc.writelines(newpkg)
                    newsrc.writelines(content[1:])
                    newsrc.flush()
                    newsrc.close()

    else:
        print 'pleaes input parameters [dirname on desktop] [surfixname like "individual" "commual"]'

if __name__ == "__main__":
    main()
