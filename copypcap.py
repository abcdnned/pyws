import sys
from shutil import copyfile
import os


def main():
    newname=sys.argv[2]
    flod=sys.argv[1]
    root='c:/Users/tom.yang/Desktop/'
    to='d:/gitrepo/dcd-pcap/'
    fd=os.path.join(root,flod)
    for parent,dirs,files in os.walk(fd):
        for f in files:
            if f.endswith('pcap'):
                copyfile(os.path.join(parent,f),os.path.join(to,newname))
                print 'copy success!'

if __name__ == "__main__":
    main()
