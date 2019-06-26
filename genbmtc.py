#-*-coding:utf-8-*-

from jinja2 import Environment,FileSystemLoader
from os.path import join
import os.path
import os
import sys
from shutil import copyfile
import shutil

#settings
tpath='/home/tom/gitrepo/pyws/bmtemplates'
oldpath='/home/tom/tmp/testcase/secj1'
bmpath='/home/tom/gitrepo/dcd/dcd-benchmark/decoder/'

#settings

def getconfig(p):
    l = ""
    f = open(p)
    a = False
    for line in f:
        if '<group' in line:
            a = True
        if '</group' in line:
            l += line
            a = False
        if a:
            l += line
    f.close()
    return l

def createconfig(dd, config):
    l=''
    with open(join(tpath,'btr.decode.xml')) as f:
        for line in f:
            if '</decode>' in line:
                l += config
            l += line
    with open(join(dd,'btr.decode.xml'),'w') as f:
        f.write(l)


for dirname in os.listdir(oldpath):
    p = join(oldpath, dirname,'btr.decode.xml')
    dd = join(bmpath, dirname)
    if (os.path.isdir(join(oldpath, dirname))):
        print dirname
        if os.path.isdir(dd):
            shutil.rmtree(dd)
        os.mkdir(dd)
        config = getconfig(p)
        createconfig(dd, config)


print "finish"
