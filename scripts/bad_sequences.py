bad_seqs = {
    'Spain/VC-IBV-98006466/2020' : "2020-03-07", # There's one spanish seq with date of 7 March - we think this is wrong.
    # There are five sequences from UK with suspected bad dates: exclude
    'England/LIVE-1DD7AC/2020' : "2020-03-10",
    'England/PORT-2D2111/2020' : "2020-03-21",
    'England/CAMB-1BA110/2020' : "2020-06-11", # suspected that these ones have reversed dd-mm (are actually 5 and 6 Nov)
    'England/CAMB-1BA0F5/2020' : "2020-05-11", # suspected that these ones have reversed dd-mm (are actually 5 and 6 Nov)
    'England/CAMB-1BA0B9/2020' : "2020-05-11", # suspected that these ones have reversed dd-mm (are actually 5 and 6 Nov)
    'Denmark/DCGC-12020/2020'  : "2020-03-30", # this sequence is identical to other Danish seqs with sample date of Oct/Nov..
    'Netherlands/NB-EMC-279/2020'   : "2020-05-08", # seems to be date reversal of day/month
    'Italy/APU-IZSPB_321PT/2020'    : "2020-04-11", # seems to be date reversal of day/month
    'Tunisia/4107/2020' : "2020-03-18", # date seems to be wrong based on divergence
    'Tunisia/3942/2020' : "2020-03-16", # date seems to be wrong based on divergence
    'Australia/QLD1278/2020'    : "2020-03-21", #seems to be wrong date - far too diverged
    'Australia/QLD1276/2020'    : "2020-03-21", # seems to be wrong date - far too diverged
    'Sweden/20-08979/2020'  : "2020-04-06", # too divergent compared to date (seems to be day/month reversed)

    'Spain/IB-IBV-99010753/2020'    : "2020-04-21", # temporarily excluded as early date doesn't match divergence - EU1
    'Spain/IB-IBV-99010754/2020'    : "2020-04-22", # temporarily excluded as early date doesn't match divergence - EU1
    'Spain/IB-IBV-99010756/2020'    : "2020-05-11", # temporarily excluded as early date doesn't match divergence - EU1
    'Spain/IB-IBV-99010769/2020'    : "2020-06-18", # temporarily excluded as early date doesn't match divergence - EU2
    'Spain/IB-IBV-99010761/2020'    : "2020-05-29", # temporarily excluded as early date doesn't match divergence - EU2
    'Italy/LAZ-INMI-92/2020' : "2010-10-26", # year given as 2010
    'Italy/LAZ-INMI-93/2020' : "2010-10-26", # year given as 2010
    'Italy/LAZ-INMI-94/2020' : "2010-10-27", # year given as 2010
    'Italy/LAZ-INMI-95/2020' : "2010-10-27", # year given as 2010
    'England/LIVE-DCA612/2020' : "2020-03-07",  # far too diverged compared to sample date
    'Netherlands/ZE-EMC-74/2020'    : "2020-06-11", # too diverged compared to date. Suspect is 6 Nov - date reversed
    'Spain/RI-IBV-99010966/2009'    : "2009-09-30", # date typed wrong
    'Denmark/DCGC-16747/2020'   : "2020-04-20", #overdiverged compared to date
    'Tunisia/19695/2020'    : "2020-07-12", #overdivrged compared to date
    'Canada/ON-S1598/2020'  : "2020-04-09", #confirmed day-month reversal
    'SouthKorea/KDCA0367/2020'  : "2020-04-04", # too divergent given date (11)
    'Tunisia/4874/2020'     :	"2020-03-24", #overdivrged compared to date
    'Germany/SL-SU-10428507/2020'   :   "2020-03-21", #overdiverged compared to date (S98F)
    'USA/CA-CZB-13378/2020' :   "2020-05-11", #overdiverged compared to date
    'USA/CA-LACPHL-AE00055/2020'    :   "2020-07-07", #overdiverged compared to date
    'USA/CA-LACPHL-AE00059/2020'    :   "2020-07-14", #overdiverged compared to date
    'USA/CA-LACPHL-AE00058/2020'    :   "2020-07-13", #overdiverged compared to date
    'Spain/MD-IBV-99007119/2020'    :   "2020-07-28", #overdiverged compared to date
    'Spain/RI-IBV-99010963/2020'    :   "2020-11-01", #super diverged - over 40 muts
    'Spain/IB-IBV-99010765/2020'  : "2020-06-18", # overdiverged, known sequencing problem with this batch
    'Spain/IB-IBV-99010766/2020'  : "2020-06-18", # overdiverged, known sequencing problem with this batch
    'Spain/IB-IBV-99010764/2020'  : "2020-06-16", # overdiverged, known sequencing problem with this batch
    'USA/MI-MDHHS-SC23078/2021'   : "2021-02-15", #future date
    'USA/MI-MDHHS-SC23104/2021'   : "2021-12-02", #future date
    'Poland/Pomorskie_MWB_51/2021'   : "2022-01-24", # future date
    'Romania/Bucuresti408383/2021'  : "2021-12-31", # future date
    'Germany/SL-SU-10429159/2020'   :   "2020-03-04", # divergence 30+, date March! Overdiverged
    'USA/CA-LACPHL-AF00294/2020'    :   "2020-01-18", #suspect should be 2021 instead - overdiverged
    'Mexico/ROO-InDRE_243/2020' : "2020-07-06", # very overdiverged compared to date - fits in diversity of 452 cluster!
    'Spain/MD-IBV-97010024/2020' : "2020-03-19", # overdiveged compared to date - 19 muts, given date March
    'England/NOTT-246E8A/2020'   : "2020-06-01", # over diverged compared to date - 1 June but nested deep in EU1 diversity
    'France/IDF_HB_112003050333/2020'   : "2020-03-13", # over diverged compared to date - 20 muts, but 13 March
    'Spain/MD-IBV-99018532/2020' : "2020-02-14", # overdiverged compared to date - 19 muts but 14 Feb
    'Germany/SL-SU-10429159/2020' : "2020-03-24", # overdiverged: 33 muts, march 2020 date. EU2
    'Germany/BAV-PL-virotum_6ZA86/2020' : "2020-05-22", #very poor quality
    'Germany/BAV-PL-virotum_DN6S6/2020' : "2020-05-20" #very poor quality
    #'bat/Yunnan/RaTG13/2013'    : "2013-07-24" #this is RatG13 - legit, but looks weird in table
    #'bat/Yunnan/RmYN02/2019'    : "2019-06-25" # bat sequence - legit but looks weird
}
