from jinja2 import Environment,FileSystemLoader
from os.path import join
import os.path
import os

#set work directory below
type = 'bank'

tpath='/home/tom/gitrepo/pyws/dcdtemplates'
dcdpath='/home/tom/gitrepo/dcd/dcd-parser'
testpath='src/test/java/cn/com/netis/dcd/parser/regression/' + type
srcpath='src/main/java/cn/com/netis/dcd/parser/decoder/' + type

custname = "hxb"
subname = 'pre'
protocol='jsb core'
testname='JxbCoreTest'
pcapname="JXB_CORE.pcap"
decoder='ZjDecoder'
ioc = "individual"
TEST_FLODER=join(dcdpath,testpath,ioc,custname,subname)
#TEST_FLODER=join(dcdpath,testpath,custname,subname)
autoreg=False
testonly=True
regpath=join(dcdpath,srcpath,ioc,custname)

env=Environment(loader=FileSystemLoader(tpath))
testT = env.get_template('SomeTest1.java')
consT=env.get_template('Some1.java')
confT=env.get_template('conf.xml')
dcdT=env.get_template('SomeDecoder1.java')

def create(*files):
    for f in files:
        if not os.path.exists(f):
            os.makedirs(f)

parent=TEST_FLODER
conf=join(parent,'config')
expected=join(parent,'expected')
dcdsrc=join(dcdpath,srcpath,ioc,custname)

create(parent,conf,expected)

with open(join(parent,testname+'.java'),'w') as f:
    f.write(testT.render(ioc = ioc, type = type, custname = custname, subname = subname, testname = testname))

with open(join(conf,'conf.xml'),'w') as f:
    f.write(confT.render(pcapname=pcapname, protocol = protocol))

if not testonly :
    create(dcdsrc)
    with open(join(dcdsrc,decoder + '.java'), 'w') as f:
        f.write(dcdT.render(ioc = ioc, custname = custname, dcdname = decoder))
