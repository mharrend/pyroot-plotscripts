from plotutils import *
# samples
samples=[Sample('t#bar{t}',ROOT.kRed+1,'/nfs/dust/cms/user/mharrend/ttbbstudies/results/ttbar_incl/*.root',''), Sample('t#bar{t}H',ROOT.kBlue,'/nfs/dust/cms/user/mharrend/ttbbstudies/results/Tranche3_ttHbb/*.root','') ]

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






# s6j4t selection
    Plot(ROOT.TH1F("N_Jetss6j4t" ,"Number of jets s6j4t",9,-0.5,8.5),"N_Jets",s6j4t),
    Plot(ROOT.TH1F("N_BTagsMs6j4t" ,"Number of medium b-tags s6j4t",9,-0.5,8.5),"N_BTagsM",s6j4t),

    Plot(ROOT.TH1F("N_TotalTagss6j4t" ,"Number of total tags s6j4t",9,-0.5,8.5),"N_TotalTags",s6j4t),
    Plot(ROOT.TH1F("N_GoodTagss6j4t" ,"Number of good tags s6j4t",9,-0.5,8.5),"N_GoodTags",s6j4t),
    Plot(ROOT.TH1F("N_MisTagss6j4t" ,"Number of mistags s6j4t",9,-0.5,8.5),"N_MisTags",s6j4t),

    Plot(ROOT.TH1F("TTBB_GenEvt_I_TTPlusCCs6j4t" ,"TTBB_GenEvt_I_TTPlusCC s6j4t",9,-0.5,8.5),"TTBB_GenEvt_I_TTPlusCC",s6j4t),
    Plot(ROOT.TH1F("TTBB_GenEvt_I_TTPlusBBs6j4t" ,"TTBB_GenEvt_I_TTPlusBB s6j4t",9,-0.5,8.5),"TTBB_GenEvt_I_TTPlusBB",s6j4t),
    Plot(ROOT.TH1F("TTBB_GenEvt_TTxId_FromProducers6j4t" ,"TTBB_GenEvt_TTxId_FromProducer s6j4t",9,-0.5,8.5),"TTBB_GenEvt_TTxId_FromProducer",s6j4t),

    Plot(ROOT.TH1F("N_additionalTaggedJetss6j4t" ,"Number of additional tagged tags s6j4t",9,-0.5,8.5),"N_additionalTaggedJets",s6j4t),
    Plot(ROOT.TH1F("N_additionalUntaggedJetss6j4t" ,"Number of additional untagged tags s6j4t",9,-0.5,8.5),"N_additionalUntaggedJets",s6j4t),

    Plot(ROOT.TH1F("Reco_Deta_Fn_best_TTBBLikelihoods6j4t","Reco_Deta_Fn_best_TTBBLikelihood s6j4t",30,-1,3),"Reco_Deta_Fn_best_TTBBLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_Deta_Fn_best_TTBBLikelihoodTimesMEs6j4t","Reco_Deta_Fn_best_TTBBLikelihoodTimesME s6j4t",30,-1,3),"Reco_Deta_Fn_best_TTBBLikelihoodTimesME",s6j4t),
    Plot(ROOT.TH1F("Reco_Deta_TopHad_BB_best_TTBBLikelihoods6j4t","Reco_Deta_TopHad_BB_best_TTBBLikelihood s6j4t",30,-1,5),"Reco_Deta_TopHad_BB_best_TTBBLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_Deta_TopHad_BB_best_TTBBLikelihoodTimesMEs6j4t","Reco_Deta_TopHad_BB_best_TTBBLikelihoodTimesME s6j4t",30,-1,5),"Reco_Deta_TopHad_BB_best_TTBBLikelihoodTimesME",s6j4t),
    Plot(ROOT.TH1F("Reco_Deta_TopLep_BB_best_TTBBLikelihoods6j4t","Reco_Deta_TopLep_BB_best_TTBBLikelihood s6j4t",30,-1,5),"Reco_Deta_TopLep_BB_best_TTBBLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_Deta_TopLep_BB_best_TTBBLikelihoodTimesMEs6j4t","Reco_Deta_TopLep_BB_best_TTBBLikelihoodTimesME s6j4t",30,-1,5),"Reco_Deta_TopLep_BB_best_TTBBLikelihoodTimesME",s6j4t),
    Plot(ROOT.TH1F("Reco_Dr_BB_best_TTLikelihoods6j4t","Reco_Dr_BB_best_TTLikelihood s6j4t",30,-1,5),"Reco_Dr_BB_best_TTLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_Dr_BB_best_TTLikelihood_combs6j4t","Reco_Dr_BB_best_TTLikelihood_comb s6j4t",30,-1,5),"Reco_Dr_BB_best_TTLikelihood_comb",s6j4t),
    Plot(ROOT.TH1F("Reco_Higgs_M_best_TTLikelihoods6j4t","Reco_Higgs_M_best_TTLikelihood s6j4t",30,0,500),"Reco_Higgs_M_best_TTLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_Higgs_M_best_TTLikelihood_combs6j4t","Reco_Higgs_M_best_TTLikelihood_comb s6j4t",30,0,500),"Reco_Higgs_M_best_TTLikelihood_comb",s6j4t),
    Plot(ROOT.TH1F("Reco_LikelihoodRatio_best_Likelihoods6j4t","Reco_LikelihoodRatio_best_Likelihood s6j4t",30,0,3),"Reco_LikelihoodRatio_best_Likelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_LikelihoodRatio_best_LikelihoodTimesMEs6j4t","Reco_LikelihoodRatio_best_LikelihoodTimesME s6j4t",30,-1,1),"Reco_LikelihoodRatio_best_LikelihoodTimesME",s6j4t),
    Plot(ROOT.TH1F("Reco_LikelihoodRatio_best_TTLikelihoods6j4t","Reco_LikelihoodRatio_best_TTLikelihood s6j4t",30,-1,1),"Reco_LikelihoodRatio_best_TTLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_LikelihoodRatio_best_TTLikelihood_combs6j4t","Reco_LikelihoodRatio_best_TTLikelihood_comb s6j4t",30,-1,1),"Reco_LikelihoodRatio_best_TTLikelihood_comb",s6j4t),
    Plot(ROOT.TH1F("Reco_LikelihoodTimesMERatio_best_Likelihoods6j4t","Reco_LikelihoodTimesMERatio_best_Likelihood s6j4t",30,-1,1),"Reco_LikelihoodTimesMERatio_best_Likelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_LikelihoodTimesMERatio_best_LikelihoodTimesMEs6j4t","Reco_LikelihoodTimesMERatio_best_LikelihoodTimesME s6j4t",30,-1,1),"Reco_LikelihoodTimesMERatio_best_LikelihoodTimesME",s6j4t),
    Plot(ROOT.TH1F("Reco_LikelihoodTimesMERatio_best_TTLikelihoods6j4t","Reco_LikelihoodTimesMERatio_best_TTLikelihood s6j4t",30,-1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_LikelihoodTimesMERatio_best_TTLikelihood_combs6j4t","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb s6j4t",30,-1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",s6j4t),
    Plot(ROOT.TH1F("Reco_MERatio_best_Likelihoods6j4t","Reco_MERatio_best_Likelihood s6j4t",30,-1,1),"Reco_MERatio_best_Likelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_MERatio_best_LikelihoodTimesMEs6j4t","Reco_MERatio_best_LikelihoodTimesME s6j4t",30,-1,1),"Reco_MERatio_best_LikelihoodTimesME",s6j4t),
    Plot(ROOT.TH1F("Reco_MERatio_best_TTLikelihoods6j4t","Reco_MERatio_best_TTLikelihood s6j4t",30,-1,1),"Reco_MERatio_best_TTLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_MERatio_best_TTLikelihood_combs6j4t","Reco_MERatio_best_TTLikelihood_comb s6j4t",30,-1,1),"Reco_MERatio_best_TTLikelihood_comb",s6j4t),
    Plot(ROOT.TH1F("Reco_Sum_LikelihoodRatios6j4t","Reco_Sum_LikelihoodRatio s6j4t",30,-1,1),"Reco_Sum_LikelihoodRatio",s6j4t),
    Plot(ROOT.TH1F("Reco_Sum_LikelihoodTimesMERatios6j4t","Reco_Sum_LikelihoodTimesMERatio s6j4t",30,-1,1),"Reco_Sum_LikelihoodTimesMERatio",s6j4t),
    Plot(ROOT.TH1F("Reco_Sum_MERatios6j4t","Reco_Sum_MERatio s6j4t",30,-1,1),"Reco_Sum_MERatio",s6j4t),
    Plot(ROOT.TH1F("Reco_Sum_TTBBLikelihoods6j4t","Reco_Sum_TTBBLikelihood s6j4t",30,-1,1),"Reco_Sum_TTBBLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_Sum_TTBBLikelihoodTimesMEs6j4t","Reco_Sum_TTBBLikelihoodTimesME s6j4t",30,-1,1),"Reco_Sum_TTBBLikelihoodTimesME",s6j4t),
    Plot(ROOT.TH1F("Reco_Sum_TTBBMEs6j4t","Reco_Sum_TTBBME s6j4t",30,-1,1),"Reco_Sum_TTBBME",s6j4t),
    Plot(ROOT.TH1F("Reco_Sum_TTHBBMEs6j4t","Reco_Sum_TTHBBME s6j4t",30,-1,1),"Reco_Sum_TTHBBME",s6j4t),
    Plot(ROOT.TH1F("Reco_Sum_TTHLikelihoods6j4t","Reco_Sum_TTHLikelihood s6j4t",30,-1,1),"Reco_Sum_TTHLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_Sum_TTHLikelihoodTimesMEs6j4t","Reco_Sum_TTHLikelihoodTimesME s6j4t",30,-1,1),"Reco_Sum_TTHLikelihoodTimesME",s6j4t),

    Plot(ROOT.TH1F("Reco_highest_TopAndWHadLikelihoods6j4t","Reco_highest_TopAndWHadLikelihood s6j4t",30,-1,1),"Reco_highest_TopAndWHadLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_highest_TTBBLikelihoods6j4t","Reco_highest_TTBBLikelihood s6j4t",30,-1,1),"Reco_highest_TTBBLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_highest_TTBBLikelihoodTimesMEs6j4t","Reco_highest_TTBBLikelihoodTimesME s6j4t",30,-1,1),"Reco_highest_TTBBLikelihoodTimesME",s6j4t),
    Plot(ROOT.TH1F("Reco_highest_TTHLikelihoods6j4t","Reco_highest_TTHLikelihood s6j4t",30,-1,1),"Reco_highest_TTHLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_highest_TTHLikelihoodTimesMEs6j4t","Reco_highest_TTHLikelihoodTimesME s6j4t",30,-1,1),"Reco_highest_TTHLikelihoodTimesME",s6j4t),
    Plot(ROOT.TH1F("Reco_highest_TTLikelihoods6j4t","Reco_highest_TTLikelihood s6j4t",30,-1,1),"Reco_highest_TTLikelihood",s6j4t),
    Plot(ROOT.TH1F("Reco_highest_TTLikelihood_combs6j4t","Reco_highest_TTLikelihood_comb s6j4t",30,-1,1),"Reco_highest_TTLikelihood_comb",s6j4t),

# No selection
    Plot(ROOT.TH1F("N_Jets" ,"Number of jets ",9,-0.5,8.5),"N_Jets",),
    Plot(ROOT.TH1F("N_BTagsM" ,"Number of medium b-tags ",9,-0.5,8.5),"N_BTagsM",),

    Plot(ROOT.TH1F("N_TotalTags" ,"Number of total tags ",9,-0.5,8.5),"N_TotalTags",),
    Plot(ROOT.TH1F("N_GoodTags" ,"Number of good tags ",9,-0.5,8.5),"N_GoodTags",),
    Plot(ROOT.TH1F("N_MisTags" ,"Number of mistags ",9,-0.5,8.5),"N_MisTags",),

    Plot(ROOT.TH1F("TTBB_GenEvt_I_TTPlusCC" ,"TTBB_GenEvt_I_TTPlusCC ",9,-0.5,8.5),"TTBB_GenEvt_I_TTPlusCC",),
    Plot(ROOT.TH1F("TTBB_GenEvt_I_TTPlusBB" ,"TTBB_GenEvt_I_TTPlusBB ",9,-0.5,8.5),"TTBB_GenEvt_I_TTPlusBB",),
    Plot(ROOT.TH1F("TTBB_GenEvt_TTxId_FromProducer" ,"TTBB_GenEvt_TTxId_FromProducer ",9,-0.5,8.5),"TTBB_GenEvt_TTxId_FromProducer",),

    Plot(ROOT.TH1F("N_additionalTaggedJets" ,"Number of additional tagged tags ",9,-0.5,8.5),"N_additionalTaggedJets",),
    Plot(ROOT.TH1F("N_additionalUntaggedJets" ,"Number of additional untagged tags ",9,-0.5,8.5),"N_additionalUntaggedJets",),

    Plot(ROOT.TH1F("Reco_Deta_Fn_best_TTBBLikelihood","Reco_Deta_Fn_best_TTBBLikelihood ",30,-1,3),"Reco_Deta_Fn_best_TTBBLikelihood",),
    Plot(ROOT.TH1F("Reco_Deta_Fn_best_TTBBLikelihoodTimesME","Reco_Deta_Fn_best_TTBBLikelihoodTimesME ",30,-1,3),"Reco_Deta_Fn_best_TTBBLikelihoodTimesME",),
    Plot(ROOT.TH1F("Reco_Deta_TopHad_BB_best_TTBBLikelihood","Reco_Deta_TopHad_BB_best_TTBBLikelihood ",30,-1,5),"Reco_Deta_TopHad_BB_best_TTBBLikelihood",),
    Plot(ROOT.TH1F("Reco_Deta_TopHad_BB_best_TTBBLikelihoodTimesME","Reco_Deta_TopHad_BB_best_TTBBLikelihoodTimesME ",30,-1,5),"Reco_Deta_TopHad_BB_best_TTBBLikelihoodTimesME",),
    Plot(ROOT.TH1F("Reco_Deta_TopLep_BB_best_TTBBLikelihood","Reco_Deta_TopLep_BB_best_TTBBLikelihood ",30,-1,5),"Reco_Deta_TopLep_BB_best_TTBBLikelihood",),
    Plot(ROOT.TH1F("Reco_Deta_TopLep_BB_best_TTBBLikelihoodTimesME","Reco_Deta_TopLep_BB_best_TTBBLikelihoodTimesME ",30,-1,5),"Reco_Deta_TopLep_BB_best_TTBBLikelihoodTimesME",),
    Plot(ROOT.TH1F("Reco_Dr_BB_best_TTLikelihood","Reco_Dr_BB_best_TTLikelihood ",30,-1,5),"Reco_Dr_BB_best_TTLikelihood",),
    Plot(ROOT.TH1F("Reco_Dr_BB_best_TTLikelihood_comb","Reco_Dr_BB_best_TTLikelihood_comb ",30,-1,5),"Reco_Dr_BB_best_TTLikelihood_comb",),
    Plot(ROOT.TH1F("Reco_Higgs_M_best_TTLikelihood","Reco_Higgs_M_best_TTLikelihood ",30,0,500),"Reco_Higgs_M_best_TTLikelihood",),
    Plot(ROOT.TH1F("Reco_Higgs_M_best_TTLikelihood_comb","Reco_Higgs_M_best_TTLikelihood_comb ",30,0,500),"Reco_Higgs_M_best_TTLikelihood_comb",),
    Plot(ROOT.TH1F("Reco_LikelihoodRatio_best_Likelihood","Reco_LikelihoodRatio_best_Likelihood ",30,0,3),"Reco_LikelihoodRatio_best_Likelihood",),
    Plot(ROOT.TH1F("Reco_LikelihoodRatio_best_LikelihoodTimesME","Reco_LikelihoodRatio_best_LikelihoodTimesME ",30,-1,1),"Reco_LikelihoodRatio_best_LikelihoodTimesME",),
    Plot(ROOT.TH1F("Reco_LikelihoodRatio_best_TTLikelihood","Reco_LikelihoodRatio_best_TTLikelihood ",30,-1,1),"Reco_LikelihoodRatio_best_TTLikelihood",),
    Plot(ROOT.TH1F("Reco_LikelihoodRatio_best_TTLikelihood_comb","Reco_LikelihoodRatio_best_TTLikelihood_comb ",30,-1,1),"Reco_LikelihoodRatio_best_TTLikelihood_comb",),
    Plot(ROOT.TH1F("Reco_LikelihoodTimesMERatio_best_Likelihood","Reco_LikelihoodTimesMERatio_best_Likelihood ",30,-1,1),"Reco_LikelihoodTimesMERatio_best_Likelihood",),
    Plot(ROOT.TH1F("Reco_LikelihoodTimesMERatio_best_LikelihoodTimesME","Reco_LikelihoodTimesMERatio_best_LikelihoodTimesME ",30,-1,1),"Reco_LikelihoodTimesMERatio_best_LikelihoodTimesME",),
    Plot(ROOT.TH1F("Reco_LikelihoodTimesMERatio_best_TTLikelihood","Reco_LikelihoodTimesMERatio_best_TTLikelihood ",30,-1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood",),
    Plot(ROOT.TH1F("Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb","Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb ",30,-1,1),"Reco_LikelihoodTimesMERatio_best_TTLikelihood_comb",),
    Plot(ROOT.TH1F("Reco_MERatio_best_Likelihood","Reco_MERatio_best_Likelihood ",30,-1,1),"Reco_MERatio_best_Likelihood",),
    Plot(ROOT.TH1F("Reco_MERatio_best_LikelihoodTimesME","Reco_MERatio_best_LikelihoodTimesME ",30,-1,1),"Reco_MERatio_best_LikelihoodTimesME",),
    Plot(ROOT.TH1F("Reco_MERatio_best_TTLikelihood","Reco_MERatio_best_TTLikelihood ",30,-1,1),"Reco_MERatio_best_TTLikelihood",),
    Plot(ROOT.TH1F("Reco_MERatio_best_TTLikelihood_comb","Reco_MERatio_best_TTLikelihood_comb ",30,-1,1),"Reco_MERatio_best_TTLikelihood_comb",),
    Plot(ROOT.TH1F("Reco_Sum_LikelihoodRatio","Reco_Sum_LikelihoodRatio ",30,-1,1),"Reco_Sum_LikelihoodRatio",),
    Plot(ROOT.TH1F("Reco_Sum_LikelihoodTimesMERatio","Reco_Sum_LikelihoodTimesMERatio ",30,-1,1),"Reco_Sum_LikelihoodTimesMERatio",),
    Plot(ROOT.TH1F("Reco_Sum_MERatio","Reco_Sum_MERatio ",30,-1,1),"Reco_Sum_MERatio",),
    Plot(ROOT.TH1F("Reco_Sum_TTBBLikelihood","Reco_Sum_TTBBLikelihood ",30,-1,1),"Reco_Sum_TTBBLikelihood",),
    Plot(ROOT.TH1F("Reco_Sum_TTBBLikelihoodTimesME","Reco_Sum_TTBBLikelihoodTimesME ",30,-1,1),"Reco_Sum_TTBBLikelihoodTimesME",),
    Plot(ROOT.TH1F("Reco_Sum_TTBBME","Reco_Sum_TTBBME ",30,-1,1),"Reco_Sum_TTBBME",),
    Plot(ROOT.TH1F("Reco_Sum_TTHBBME","Reco_Sum_TTHBBME ",30,-1,1),"Reco_Sum_TTHBBME",),
    Plot(ROOT.TH1F("Reco_Sum_TTHLikelihood","Reco_Sum_TTHLikelihood ",30,-1,1),"Reco_Sum_TTHLikelihood",),
    Plot(ROOT.TH1F("Reco_Sum_TTHLikelihoodTimesME","Reco_Sum_TTHLikelihoodTimesME ",30,-1,1),"Reco_Sum_TTHLikelihoodTimesME",),

    Plot(ROOT.TH1F("Reco_highest_TopAndWHadLikelihood","Reco_highest_TopAndWHadLikelihood ",30,-1,1),"Reco_highest_TopAndWHadLikelihood",),
    Plot(ROOT.TH1F("Reco_highest_TTBBLikelihood","Reco_highest_TTBBLikelihood ",30,-1,1),"Reco_highest_TTBBLikelihood",),
    Plot(ROOT.TH1F("Reco_highest_TTBBLikelihoodTimesME","Reco_highest_TTBBLikelihoodTimesME ",30,-1,1),"Reco_highest_TTBBLikelihoodTimesME",),
    Plot(ROOT.TH1F("Reco_highest_TTHLikelihood","Reco_highest_TTHLikelihood ",30,-1,1),"Reco_highest_TTHLikelihood",),
    Plot(ROOT.TH1F("Reco_highest_TTHLikelihoodTimesME","Reco_highest_TTHLikelihoodTimesME ",30,-1,1),"Reco_highest_TTHLikelihoodTimesME",),
    Plot(ROOT.TH1F("Reco_highest_TTLikelihood","Reco_highest_TTLikelihood ",30,-1,1),"Reco_highest_TTLikelihood",),
    Plot(ROOT.TH1F("Reco_highest_TTLikelihood_comb","Reco_highest_TTLikelihood_comb ",30,-1,1),"Reco_highest_TTLikelihood_comb",),

]

listOfhistoLists=createHistoLists_fromTree(plots,samples,'MVATree')
writeListOfHistoLists(listOfhistoLists,samples,"ttbar vs. ttH", "ttbbRecoLikelihoodStudien2")

