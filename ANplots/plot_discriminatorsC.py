import sys
import os
sys.path.insert(0, '../')
from scriptgenerator import *
from plotutils import *
from plotconfig import *


name='discrplotsC'
sel_singleel="(N_LooseMuons==0)" # need to veto muon events in electron dataset to avoid double countung
sel_singlemu="(N_LooseElectrons==0)" # and vice versa...

mcweight='2.0*2.61*(Evt_Odd==0)'
nhistobins_=      [ 20,       10,     20,       10,   20,   20,  10    ]
minxvals_=        [-0.9,   -0.35,  -0.8, -0.75,   -0.80,  -0.8, -0.6]
maxxvals_=        [0.8,     0.5,  0.8,    0.75,    0.76,   0.8,   0.7]
discrs =          ['/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_43_MEMBDTv2.xml', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_44_MEMBDTv2.xml', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_53_MEMBDTv2.xml', '/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_54_MEMBDTv2.xml' , 'BDT_common5_output','/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_63_MEMBDTv2.xml','/nfs/dust/cms/user/kelmorab/MEMstudies/3makeHistosAndCards/weights/weights_Final_64_MEMBDTv2.xml']

nhistobins=[]
minxvals=[]
maxxvals=[]
for n in nhistobins_:
  nhistobins.append(n)
for x in minxvals_:
  minxvals.append(x)
for x in maxxvals_:
  maxxvals.append(x)

categories_=[("(N_Jets==4&&N_BTagsM==3)","4 jets, 3 b-tags","s43"),
            ("(N_Jets==4&&N_BTagsM>=4)","4 jets, #geq4 b-tags","s44"),
            ("(N_Jets==5&&N_BTagsM==3)","5 jets, 3 b-tags","s53"),
            ("(N_Jets==5&&N_BTagsM>=4)","5 jets, #geq4 b-tags","s54"),
            ("(N_Jets>=6&&N_BTagsM==2)","#geq6 jets, 2 b-tags","s62"),
            ("(N_Jets>=6&&N_BTagsM==3)","#geq6 jets, 3 b-tags","s63"),
            ("(N_Jets>=6&&N_BTagsM>=4)","#geq6 jets, #geq4 b-tags","s64")]
categories=[]
bdtcuts=[0.2,0.2,0.1,0.2,0.1,0.1,0.1]

for cat,bdt in zip(categories_,bdtcuts):
    categories.append(cat )
print categories
bins= [c[0] for c in categories]
binlabels= [c[1] for c in categories]
binnames= [c[2] for c in categories]


# data samples (name, color, path to files, selection, nickname_without_special_characters,optional: number of events for cross check)
samples_data=samples_data_bdtplots
samples=samplesBDTplots

plots=[]
print len(discrs),len(bins),len(binlabels),len(nhistobins),len(minxvals),len(maxxvals),
print len(zip(discrs,bins,binlabels,nhistobins,minxvals,maxxvals))
for discr,b,bl,bn,nb,minx,maxx in zip(discrs,bins,binlabels,binnames,nhistobins,minxvals,maxxvals):
  if '.xml' in discr:
    plots.append(MVAPlot(ROOT.TH1F("BDT_"+bn,"BDT containing MEM",nb,minx,maxx),discr,b,bl))
  elif 'common' in discr:
    plots.append(Plot(ROOT.TH1F("BDT_"+bn,"BDT discriminator",nb,minx,maxx),discr,b,bl))
  else:
    plots.append(Plot(ROOT.TH1F("BDT_"+bn,"MEM discriminator",nb,minx,maxx),discr,b,bl))
  print discr,b,bl,nb,minx,maxx

# plot parallel -- alternatively there are also options to plot more traditional that also return lists of histo lists
outputpath=plotParallel(name,2000000,plots,samples+samples_data)
listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCan(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name,False,labels,True,True)

listOfHistoLists=createHistoLists_fromSuperHistoFile(outputpath,samples,plots,1)
listOfHistoListsData=createHistoLists_fromSuperHistoFile(outputpath,samples_data,plots,1)
labels=[plot.label for plot in plots]
lolT=transposeLOL(listOfHistoLists)
plotDataMCan(listOfHistoListsData,transposeLOL(lolT[1:]),samples[1:],lolT[0],samples[0],20,name+'_log',True,labels,True,True)
