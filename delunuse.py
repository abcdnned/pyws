import os
import os.path

ws="d:/gitrepo/dcd/dcd-parser/src/main/java/"


report='d:/eclipsews/workspace/ucdetector_reports/UCDetectorReport_001.txt'
i=open(report)
lines=i.readlines()

defs=''

paths=[]

for line in lines:
    e=line.find('.<init>')
    if e>0:
        path=line[:e].replace('.','/')
        if path.endswith('DecoderManager') or path.endswith('ProtocolManager'):
            paths.append(path+'.java')

i.close()

for l in paths:
    os.remove(ws+l)


