from plotutils import *

s6j4t="(N_Jets>=6&&N_BTagsM>=4)"

# Jet pt select
jetpT25='(Jet_Pt>35 && Jet_GenJet_Pt>25)'
jetpT20='(Jet_Pt>35 && Jet_GenJet_Pt>20)'

# samples
samples=[Sample('t#bar{t}+b#bar{b}',ROOT.kRed+1,'/nfs/dust/cms/user/mharrend/ttbbstudies/results/ttbb_sl/*.root',jetpT20), Sample('t#bar{t}+b#bar{b}2',ROOT.kBlue,'/nfs/dust/cms/user/mharrend/ttbbstudies/results/ttbb_sl/*.root',jetpT25) ]



plots=[

# No selection
    Plot(ROOT.TH1F("N_Jets" ,"Number of jets ",13,-0.5,12.5),"N_Jets",),
    Plot(ROOT.TH1F("N_BTagsM" ,"Number of medium b-tags ",9,-0.5,8.5),"N_BTagsM",),
   
    Plot(ROOT.TH1F("N_TotalTags" ,"Number of total tags ",9,-0.5,8.5),"N_TotalTags",),
    Plot(ROOT.TH1F("N_GoodTags" ,"Number of good tags ",9,-0.5,8.5),"N_GoodTags",),
    Plot(ROOT.TH1F("N_MisTags" ,"Number of mistags ",9,-0.5,8.5),"N_MisTags",),




# s6j4t selection
    Plot(ROOT.TH1F("N_Jetss6j4t" ,"Number of jets s6j4t",13,-0.5,12.5),"N_Jets",s6j4t),
    Plot(ROOT.TH1F("N_BTagsMs6j4t" ,"Number of medium b-tags s6j4t",9,-0.5,8.5),"N_BTagsM",s6j4t),

    Plot(ROOT.TH1F("N_TotalTagss6j4t" ,"Number of total tags ",9,-0.5,8.5),"N_TotalTags",s6j4t),
    Plot(ROOT.TH1F("N_GoodTagss6j4t" ,"Number of good tags ",9,-0.5,8.5),"N_GoodTags",s6j4t),
    Plot(ROOT.TH1F("N_MisTagss6j4t" ,"Number of mistags ",9,-0.5,8.5),"N_MisTags",s6j4t),
 
]

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfHistoLists(listOfhistoLists,samples,"ttbb (GenjetPt > 20 GeV vs. ttbb (GenjetPt > 25 GeV)", "ttbbttbbComparison7")






