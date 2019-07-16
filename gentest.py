from jinja2 import Environment,FileSystemLoader
from os.path import join
import os.path
import os
import sys
from shutil import copyfile
import shutil
from subprocess import call

#settings
type = 'bank'

tpath='/home/tom/gitrepo/pyws/dcdtemplates'
dcdpath='/home/tom/gitrepo/dcd/dcd-parser'
pcappath='/home/tom/gitrepo/dcd-pcap/'
protopath='/home/tom/gitrepo/protocols/'
testpath='src/test/java/cn/com/netis/dcd/parser/regression/' + type
srcpath='src/main/java/cn/com/netis/dcd/parser/decoder/' + type
refpath='/home/tom/dcdreq'

#settings
pcapname="CCCB_B2B.pcap"
protoname='bank/cgb/CGB PAY APP'
uploadproto=False
uploadpcap=False
addnewcase=False
casename="credit"
custname = "cccb"
subname = 'b2b'
testname ='CccbB2bTest'
ioc = "individual"
TEST_FLODER=join(dcdpath,testpath,ioc,custname,subname)
#TEST_FLODER=join(dcdpath,testpath,ioc,"supplier",custname,subname)
# TEST_FLODER=join(dcdpath,testpath,custname)
#TEST_FLODER=join(dcdpath,testpath,custname,subname)
regpath=join(dcdpath,srcpath,ioc,custname)
dcdsrc=join(dcdpath,srcpath,ioc,custname)

location = TEST_FLODER.replace('/','.')
location = location[location.find('regression') + len('regression') + 1:]

mt = 0
fn = ''
for dirname in os.listdir(refpath):
    p = join(refpath, dirname)
    m = os.path.getmtime(p)
    if not dirname.startswith('.') and m > mt:
        mt = m
        fn = p

if uploadproto:
    shutil.copytree(fn, join(protopath,protoname))
    call(['git','-C',protopath,'pull'])
    call(['git','-C',protopath,'add','-A'])
    call(['git','-C',protopath,'commit','-m','"upload"'])
    call(['git','-C',protopath,'push'])

mc = []
mt = []
page = 20


def collect():
    c = 0
    for root, dirs, files in os.walk(fn):
        for f in files:
            if f.endswith('.pcap'):
                c += 1
                p = join(root, f)
                mc.append(p)
                mt.append(os.path.getmtime(p))
                if c == 20:
                    return

def mkconf():
    for root, dirs, files in os.walk(fn):
        for f in files:
            if f == 'dp.xml':
                p = join(root, f)
                fr = open(p)
                s = fr.read()
                fr.close()
                print 'got configuration {} :'.format(p)
                print s
                return s
    return ''

def sort():
    i = 0
    while i < len(mt) - 1 :
        j = 0
        while j < len(mc) - i - 1 :
            if mt[j] < mt[j + 1]:
                t = mt[j]
                mt[j] = mt[j + 1]
                mt[j + 1] = t
                t = mc[j]
                mc[j] = mc[j + 1]
                mc[j + 1] = t
            j += 1
        i += 1


collect()
sort()

if len(mc) > 0 :
    x = 0
    if len(mc) > 1 :
        for i, e in enumerate(mc):
            print '{} {}'.format(i, e)
        x = int(raw_input("please enter the file index: "))
    dst = join(pcappath, pcapname)
    copyfile(mc[x], dst)
    print 'copy file {} to {}'.format(mc[x], dst)
    if uploadpcap :
        call(['git','-C',pcappath,'pull'])
        call(['git','-C',pcappath,'add','-A'])
        call(['git','-C',pcappath,'commit','-m','"upload"'])
        call(['git','-C',pcappath,'push'])

protocols = mkconf()


env=Environment(loader=FileSystemLoader(tpath))
testT = env.get_template('SomeTest1.java')
confT=env.get_template('conf.xml')

def create(*files):
    for f in files:
        if not os.path.exists(f):
            os.makedirs(f)

parent=TEST_FLODER
conf=join(parent,'config')
expected=join(parent,'expected')

create(parent,conf,expected)
create(join(expected, casename))

def genTestCase(name):
    t = '    @Test\n    public final void test{}() throws IOException {{\n        SUITE.play("{}");\n    }}\n\n'
    return t.format(name.title(), name)

def getTestName(parent):
    for f in os.listdir(parent):
        if f.endswith('java'):
            return f
    return ""

if addnewcase:
    tf = getTestName(parent)
    l = ""
    with open(join(parent,tf)) as f:
        for line in f:
            if 'static {' in line:
                l += genTestCase(casename)
            l += line
    with open(join(parent,tf), "w") as f:
        f.write(l)
else:
    with open(join(parent,testname+'.java'),'w') as f:
        f.write(testT.render(location = location, testname = testname))

if addnewcase:
    with open(join(conf,'{}.conf.xml'.format(casename)),'w') as f:
        f.write(confT.render(pcapname=pcapname, protocols = protocols))
else:
    with open(join(conf,'conf.xml'),'w') as f:
        f.write(confT.render(pcapname=pcapname, protocols = protocols))


print 'config file generated'
