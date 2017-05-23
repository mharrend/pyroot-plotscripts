from plotutils import *




# selecion for categories
s4j3t="(N_Jets==4&&N_BTagsM==3)"
s4j3tbb0="(N_Jets==4 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==0)"
s4j3tbb1="(N_Jets==4 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==1)"
s4j3tbb2="(N_Jets==4 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==2)"
s4j3tbb3="(N_Jets==4 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==3)"

s4j4t="(N_Jets==4&&N_BTagsM>=4)"
s4j4tbb0="(N_Jets==4 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==0)"
s4j4tbb1="(N_Jets==4 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==1)"
s4j4tbb2="(N_Jets==4 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==2)"
s4j4tbb3="(N_Jets==4 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==3)"

s5j3t="(N_Jets==5&&N_BTagsM==3)"
s5j3tbb0="(N_Jets==5 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==0)"
s5j3tbb1="(N_Jets==5 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==1)"
s5j3tbb2="(N_Jets==5 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==2)"
s5j3tbb3="(N_Jets==5 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==3)"

s5j4t="(N_Jets==5&&N_BTagsM>=4)"
s5j4tbb0="(N_Jets==5 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==0)"
s5j4tbb1="(N_Jets==5 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==1)"
s5j4tbb2="(N_Jets==5 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==2)"
s5j4tbb3="(N_Jets==5 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==3)"

s6j2t="(N_Jets>=6&&N_BTagsM==2)"
s6j2tbb0="(N_Jets==6 && N_BTagsM==2 && TTBB_GenEvt_I_TTPlusBB==0)"
s6j2tbb1="(N_Jets==6 && N_BTagsM==2 && TTBB_GenEvt_I_TTPlusBB==1)"
s6j2tbb2="(N_Jets==6 && N_BTagsM==2 && TTBB_GenEvt_I_TTPlusBB==2)"
s6j2tbb3="(N_Jets==6 && N_BTagsM==2 && TTBB_GenEvt_I_TTPlusBB==3)"

s6j3t="(N_Jets>=6&&N_BTagsM==3)"
s6j3tbb0="(N_Jets==6 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==0)"
s6j3tbb1="(N_Jets==6 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==1)"
s6j3tbb2="(N_Jets==6 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==2)"
s6j3tbb3="(N_Jets==6 && N_BTagsM==3 && TTBB_GenEvt_I_TTPlusBB==3)"

s6j4t="(N_Jets>=6&&N_BTagsM>=4)"
s6j4tbb0="(N_Jets==6 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==0)"
s6j4tbb1="(N_Jets==6 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==1)"
s6j4tbb2="(N_Jets==6 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==2)"
s6j4tbb3="(N_Jets==6 && N_BTagsM==4 && TTBB_GenEvt_I_TTPlusBB==3)"


# Jet pt select
jetpT30='(Jet_Pt>35 && Jet_GenJet_Pt>30 && GenEvt_I_TTPlusBB==3)'
jetpT20='(Jet_Pt>35 && Jet_GenJet_Pt>20 && GenEvt_I_TTPlusBB==3)'

# samples
samples=[Sample('t#bar{t}+b#bar{b} POWHEG',ROOT.kRed+1,'/nfs/dust/cms/user/matsch/ntuples/Spring17/v2/ttbar_incl/*.root',jetpT20), Sample('t#bar{t}+b#bar{b} MG5aMC',ROOT.kBlue,'/nfs/dust/cms/user/matsch/ntuples/Spring17/v2/ttbar_aMC/*.root',jetpT20) ]



plots=[

# No selection
    Plot(ROOT.TH1F("N_Jets" ,"Number of jets ",13,-0.5,12.5),"N_Jets",),
    Plot(ROOT.TH1F("N_BTagsM" ,"Number of medium b-tags ",9,-0.5,8.5),"N_BTagsM",),
   
    Plot(ROOT.TH1F("N_TotalTagsM" ,"Number of total tags ",9,-0.5,8.5),"N_TotalTagsM",),
    Plot(ROOT.TH1F("N_GoodTagsM" ,"Number of good tags ",9,-0.5,8.5),"N_GoodTagsM",),
    Plot(ROOT.TH1F("N_MisTagsM" ,"Number of mistags ",9,-0.5,8.5),"N_MisTagsM",),




# s6j4t selection
    Plot(ROOT.TH1F("N_Jetss6j4t" ,"Number of jets s6j4t",13,-0.5,12.5),"N_Jets",s6j4t),
    Plot(ROOT.TH1F("N_BTagsMs6j4t" ,"Number of medium b-tags s6j4t",9,-0.5,8.5),"N_BTagsM",s6j4t),

    Plot(ROOT.TH1F("N_TotalTagsMs6j4t" ,"Number of total tags ",9,-0.5,8.5),"N_TotalTagsM",s6j4t),
    Plot(ROOT.TH1F("N_GoodTagsMs6j4t" ,"Number of good tags ",9,-0.5,8.5),"N_GoodTagsM",s6j4t),
    Plot(ROOT.TH1F("N_MisTagsMs6j4t" ,"Number of mistags ",9,-0.5,8.5),"N_MisTagsM",s6j4t),
 
]

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfHistoLists(listOfhistoLists,samples,"ttbb POWHEG vs. ttbb MG5aMC@NLO ", "ttbbPOWttbbaMCComparison12")






