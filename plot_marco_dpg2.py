from plotutils import *
# samples
samples=[Sample('t#bar{t}+b#bar{b}',ROOT.kRed+1,'/nfs/dust/cms/user/mharrend/ttbbstudies/results/ttbb_sl/*.root',''), Sample('t#bar{t}H',ROOT.kBlue,'/nfs/dust/cms/user/mharrend/ttbbstudies/results/old/ttHbb/*.root','') ]

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

plots=[

# No selection
    Plot(ROOT.TH1F("N_Jets" ,"Number of jets ",13,-0.5,12.5),"N_Jets",),
    Plot(ROOT.TH1F("N_BTagsM" ,"Number of medium b-tags ",9,-0.5,8.5),"N_BTagsM",),

    Plot(ROOT.TH1F("Jet_Pt" ,"jet pt",50,0,500),"Jet_Pt",),
    Plot(ROOT.TH1F("Jet_Pt1" ,"1st jet pt",40,0,800),"Jet_Pt[0]",),
    Plot(ROOT.TH1F("Jet_Pt2" ,"2nd jet pt",40,0,800),"Jet_Pt[1]",),
    Plot(ROOT.TH1F("Jet_Pt3" ,"3rd jet pt",40,0,400),"Jet_Pt[2]",),
    Plot(ROOT.TH1F("Jet_Pt4" ,"4th jet pt",40,0,400),"Jet_Pt[3]",),
    Plot(ROOT.TH1F("Jet_Pt5" ,"5th jet pt",20,0,200),"Jet_Pt[4]",),
    Plot(ROOT.TH1F("Jet_Pt6" ,"6th jet pt",20,0,200),"Jet_Pt[5]",),
    Plot(ROOT.TH1F("Jet_Eta" ,"jet #eta",50,-2.5,2.5),"Jet_Eta",),
    Plot(ROOT.TH1F("Jet_CSV" ,"CSVv2 IVF all jets",40,0,1),"Jet_CSV",),
    Plot(ROOT.TH1F("Jet_CSVb" ,"CSVv2 IVF b-jets",40,0,1),"Jet_CSV","abs(Jet_Flav)>4.5"),
    Plot(ROOT.TH1F("Jet_CSVc" ,"CSVv2 IVF c-jets",40,0,1),"Jet_CSV","abs(Jet_Flav)>3.5&&abs(Jet_Flav)<4.5"),
    Plot(ROOT.TH1F("Jet_CSVl" ,"CSVv2 IVF l-jets",40,0,1),"Jet_CSV","abs(Jet_Flav)<3.5"),
    Plot(ROOT.TH1F("Jet_Charge" ,"jet charge",50,-1,1),"Jet_Charge",),
    Plot(ROOT.TH1F("Jet_M" ,"jet mass",50,0,50),"Jet_M",),
 
    Plot(ROOT.TH1F("N_TotalTags" ,"Number of total tags ",9,-0.5,8.5),"N_TotalTags",),
    Plot(ROOT.TH1F("N_GoodTags" ,"Number of good tags ",9,-0.5,8.5),"N_GoodTags",),
    Plot(ROOT.TH1F("N_MisTags" ,"Number of mistags ",9,-0.5,8.5),"N_MisTags",),




# s6j4t selection
    Plot(ROOT.TH1F("N_Jetss6j4t" ,"Number of jets s6j4t",13,-0.5,12.5),"N_Jets",s6j4t),
    Plot(ROOT.TH1F("N_BTagsMs6j4t" ,"Number of medium b-tags s6j4t",9,-0.5,8.5),"N_BTagsM",s6j4t),

    Plot(ROOT.TH1F("Jet_Pts6j4t" ,"jet pts6j4t",50,0,500),"Jet_Pt",s6j4t),
    Plot(ROOT.TH1F("Jet_Pt1s6j4t" ,"1st jet pts6j4t",40,0,800),"Jet_Pt[0]",s6j4t),
    Plot(ROOT.TH1F("Jet_Pt2s6j4t" ,"2nd jet pts6j4t",40,0,800),"Jet_Pt[1]",s6j4t),
    Plot(ROOT.TH1F("Jet_Pt3s6j4t" ,"3rd jet pts6j4t",40,0,400),"Jet_Pt[2]",s6j4t),
    Plot(ROOT.TH1F("Jet_Pt4s6j4t" ,"4th jet pts6j4t",40,0,400),"Jet_Pt[3]",s6j4t),
    Plot(ROOT.TH1F("Jet_Pt5s6j4t" ,"5th jet pts6j4t",20,0,200),"Jet_Pt[4]",s6j4t),
    Plot(ROOT.TH1F("Jet_Pt6s6j4t" ,"6th jet pts6j4t",20,0,200),"Jet_Pt[5]",s6j4t),
    Plot(ROOT.TH1F("Jet_Etas6j4t" ,"jet #etas6j4t",50,-2.5,2.5),"Jet_Eta",s6j4t),
    Plot(ROOT.TH1F("Jet_CSVs6j4t" ,"CSVv2 IVF all jetss6j4t",40,0,1),"Jet_CSV",s6j4t),
    Plot(ROOT.TH1F("Jet_Charges6j4t" ,"jet charges6j4t",50,-1,1),"Jet_Charge",s6j4t),
    Plot(ROOT.TH1F("Jet_Ms6j4t" ,"jet masss6j4t",50,0,50),"Jet_M",s6j4t),
  
 
]

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfHistoLists(listOfhistoLists,samples,"ttbb vs. ttH", "ttbbttHComparison2")






