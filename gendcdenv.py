from jinja2 import Environment,FileSystemLoader
from os.path import join
import os.path
import os

#set work directory below
tpath='/home/tom/gitrepo/pyws/dcdtemplates'
dcdpath='/home/tom/gitrepo/dcd/dcd-parser'
testpath='src/test/java/cn/com/netis/dcd/parser/regression/bank'
srcpath='src/main/java/cn/com/netis/dcd/parser/decoder/bank'

#set parameters below
bankname='hxb'
pkgname='pos'
protocol='\"hxb pos\"'
testname='HxbPosTest'
pcapname="HXB_POX.pcap"
decoder='SmsDecoder'
TEST_FLODER=join(dcdpath,testpath,bankname,pkgname)
autoreg=False
regtype='bank'
testonly=True
mngfloder=join(dcdpath,srcpath,bankname)

env=Environment(loader=FileSystemLoader(tpath))
testT = env.get_template('SomeTest.java')
fileT=env.get_template('file.xml')
decodeT=env.get_template('btr.decode.xml')
consT=env.get_template('Some.java')
exportT=env.get_template('btr.export.xml')
dpT=env.get_template('dataprovider.xml')
dcdT=env.get_template('SomeDecoder.java')

def doautoreg(root,basename,regname,rf,protmngn):
    #register to BankProtocols.java
    try:
        f=open(join(dcdpath,srcpath,'{}.java'.format(protmngn)),'r')
        lines=f.readlines()
        flag=0
        start=-1
        nxt=-1
        for i,line in enumerate(lines):
            if basename+' +' in line:
                flag=3
                start=i
                nxt=int(line[line.find('+')+2:line.rfind(';')])+1
            elif flag>0:
                flag-=1
                if flag<=0:
                    break
        f.close()
        f=open(join(root,protmngn+'.java'),'w')
        f.writelines(lines[:start+1])
        f.write('\n')
        f.write('\t/** The Constant '+regname+'. **/\n')
        f.write('\tpublic static final int '+regname+' = '+basename+' + '+str(nxt)+';\n')
        f.writelines(lines[start+1:])
        #register to DecoderManager and ProtocolManager.
        for parent,dirs,files in os.walk(rf):
            for fi in files:
                if fi.endswith('DecoderManager.java'):
                    with open(join(parent,fi),'r') as f:
                        lines=f.readlines()
                        for i,line in enumerate(lines):
                            if 'return result' in line:
                                start=i
                                break
                        if start != -1:
                            f.close()
                            f=open(join(parent,fi),'w')
                            f.writelines(lines[:start])
                            f.write('\t\tresult.put({}.'.format(protmngn)+regname+', new '+decoder+'());\n')
                            f.writelines(lines[start:])
                elif fi.endswith('ProtocolManager.java'):
                    with open(join(parent,fi),'r') as f:
                        lines=f.readlines()
                        for i,line in enumerate(lines):
                            if 'return result' in line:
                                start=i
                                break
                        if start != -1:
                            f.close()
                            f=open(join(parent,fi),'w')
                            f.writelines(lines[:start])
                            f.write('\t\tresult.put({}.'.format(protmngn)+regname+', "'+protocol.strip('"')+'", '+'"'+regname+'");\n')
                            f.writelines(lines[start:])
    finally:
        f.close()

def create(*files):
    for f in files:
        if not os.path.exists(f):
            os.makedirs(f)

parent=TEST_FLODER
conf=join(parent,'config')
expected=join(parent,'expected')
dcdsrc=join(dcdpath,srcpath,bankname)

create(parent,conf,expected,dcdsrc)

pn= pkgname if regtype=='stock' else bankname
testpn="{}.{}".format(bankname,pkgname) if regtype=='bank' else pkgname

with open(join(parent,testname+'.java'),'w') as f:
    f.write(testT.render(testname=testname,rootflod=regtype,pkgname=testpn))

with open(join(conf,'file.xml'),'w') as f:
    f.write(fileT.render(pcapname=pcapname))

with open(join(conf,'btr.decode.xml'),'w') as f:
    f.write(decodeT.render(protocol=protocol))

with open(join(conf,'btr.export.xml'),'w') as f:
    f.write(exportT.render(testname=testname))

with open(join(conf,'dataprovider.xml'),'w') as f:
    f.write(dpT.render())

if not testonly:
    with open(join(dcdsrc,decoder+'.java'),'w') as f:
        f.write(dcdT.render(parent=regtype,decoder=decoder,bankname=bankname,pkgname=pn))

    cons=decoder[:-7]
    with open(join(dcdsrc,cons+'.java'),'w') as f:
        f.write(consT.render(cons=cons,bankname=bankname,parent=regtype,pkgname=pn))

    if autoreg:
        if regtype=='stock':
            basename='BASE'
            regname=bankname.upper()+'_'+pkgname
            regname=regname.upper()
            doautoreg(join(dcdpath,srcpath),basename,regname,bankname,True,'StockProtocols')
        elif regtype=='bank':
            bankbase=bankname.upper()+'_BASE'
            regname=bankname.upper()+'_'+pkgname
            regname=regname.upper()
            root=join(dcdpath,srcpath)
            doautoreg(root,bankbase,regname,mngfloder,'BankProtocols')
