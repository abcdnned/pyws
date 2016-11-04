from jinja2 import Environment ,FileSystemLoader
import sys
from shutil import copyfile
from shutil import copytree
from os.path import join
import os

ws='c:/Users/tom.yang/Desktop/'
testdir='D:/gitrepo/dcd/dcd-parser/src/test/java/'
btrconf='config/btr.decode.xml'
fileconf='config/file.xml'
type='bank'


def getNewPath(pkgline,surfix):
    npkg=pkgline.replace(type,type+'.'+surfix)
    pkg=npkg[8:-2]
    np=pkg.replace('.','/')
    return (npkg,join(testdir,np))

def findSurfixFile(root,surfix): 
    for parent,dirs,files in os.walk(root):
        for f in files:
            if f.endswith(surfix):
                return join(f)

def findStartEnd(lines,start,end):
    s=-1
    e=-1
    for i,line in enumerate(lines):
        if start in line:
            s=i
        if s>0 and end in line:
            e=i
    return (s,e)

dcdpath='d:\\gitrepo\\dcd3.4\\dcd-parser'
testpath='src\\test\\java\\cn\\com\\netis\dcd\\parser\\regression\\bank'

def main():
    if len(sys.argv)<4:
        print 'pleaes input parameters [dirname on desktop] [the test dir under pervious dir] [surfixname like "individual" "commual"]'
        return 
    dtdir=sys.argv[1]
    tdir=sys.argv[2]
    surfix=sys.argv[3]
    root=join(ws,dtdir,tdir)
    if dtdir == 'src' :
        root = join(dcdpath,testpath,tdir)
    print root
    f=findSurfixFile(root,'Test.java')
    print f
    src=open(join(root,f))
    content=src.readlines()
    src.close()
    (npkg,np)=getNewPath(content[0],surfix)
    if not os.path.exists(join(testdir,np)):
        os.makedirs(join(testdir,np))
    ntsrc=open(join(testdir,np,f),'w')
    ntsrc.writelines(npkg)
    ntsrc.writelines(content[1:])
    ntsrc.flush()
    ntsrc.close()

    bc=open(join(root,btrconf))
    bclines=bc.readlines()
    s=0
    e=0
    for i,line in enumerate(bclines):
        if '<group' in line:
            s=i
        if '</group' in line:
            e=i
    group="".join(bclines[s:e+1])

    fc=open(join(root,fileconf))
    fclines=fc.readlines()
    pcapname=''
    for line in fclines:
        if '<file' in  line:
            s=line.find('/')+1
            e=line.find('.pcap')
            pcapname=line[s:e]

    env=Environment(loader=FileSystemLoader('c:/pyws'))
    gt = env.get_template('conftemplate')


    confp=join(testdir,np,'config')
    if not os.path.exists(confp):
        os.makedirs(confp)
    with open(join(confp,'conf.xml'),'w') as f:
        f.write(gt.render(group=group,pcapname=pcapname))

    #copy expected floder
    epecdir=join(root,'expected')
    copytree(epecdir,join(testdir,np,'expected'))

if __name__ == "__main__":
    main()
