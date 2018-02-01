import configtools
import os

RUN ='GH'
JEC ='Summer16_07Aug2017H_V1'#'Summer16_07Aug2017'+RUN+'_V1'

def config():
    cfg = configtools.getConfig('data', 2016, 'mm', bunchcrossing='25ns')
    cfg["InputFiles"].set_input(
        #ekppath='/storage/c/tberger/testfiles/skimming_output/data/ZJet_SingleMuon_Run2016G-Legacy-07Aug2017-v1_testfile.root',
        ekppathF='srm://cmssrm-kit.gridka.de:8443/srm/managerv2?SFN=/pnfs/gridka.de/cms/disk-only/store/user/tberger/Skimming/ZJet_SingleMuon_Run2016F-Legacy-07Aug2017-v1/*.root',
        ekppathG='srm://cmssrm-kit.gridka.de:8443/srm/managerv2?SFN=/pnfs/gridka.de/cms/disk-only/store/user/tberger/Skimming/ZJet_SingleMuon_Run2016G-Legacy-07Aug2017-v1/*.root',
        ekppathH='srm://cmssrm-kit.gridka.de:8443/srm/managerv2?SFN=/pnfs/gridka.de/cms/disk-only/store/user/tberger/Skimming/ZJet_SingleMuon_Run2016H-Legacy-07Aug2017-v1/*.root',
    )
    
    cfg = configtools.expand(cfg, ['nocuts', 'zcuts', 'leptoncuts'], ['None'])#, True),'L1L2L3','L1L2L3Res'
    configtools.remove_quantities(cfg, ['jet1ptl1l2l3', 'jet1res', 'jet1rc'])
    # Add Muon SF and Correction Producers
    cfg['Processors'] += ['producer:LeptonSFProducer','producer:LeptonTriggerSFProducer',]#'producer:MuonTriggerMatchingProducer',
    cfg['Processors'].insert(cfg['Processors'].index('producer:ValidMuonsProducer'), 'producer:MuonCorrectionsProducer',)
    cfg['ValidMuonsInput'] = "corrected"
    # Change Trigger Requirements for SiMu Dataset
    cfg['HltPaths'] = ['HLT_IsoMu24', 'HLT_IsoTkMu24']
    cfg["MuonTriggerFilterNames"] = [
        #"HLT_IsoMu22_v2:hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09",
        #"HLT_IsoTkMu22_v2:hltL3fL1sMu20L1f0Tkf22QL3trkIsoFiltered0p09", 
        #"HLT_IsoTkMu22_v3: hltL3fL1sMu20L1f0Tkf22QL3trkIsoFiltered0p09", 
        #"HLT_IsoMu22_v3:hltL3crIsoL1sMu20L1f0L2f10QL3f22QL3trkIsoFiltered0p09",
        #"HLT_IsoTkMu22_v4:hltL3fL1sMu20L1f0Tkf22QL3trkIsoFiltered0p09"
        'HLT_IsoMu24_v2:hltL3crIsoL1sMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p09',
        'HLT_IsoTkMu24_v3:hltL3fL1sMu22L1f0Tkf24QL3trkIsoFiltered0p09'
        ]
    cfg['MuonIso'] = 'loose'
    cfg['CutMuonPtMin'] = 22.0
    cfg['VertexSummary'] = 'offlinePrimaryVerticesSummary'
    cfg['Jec'] = os.path.join(configtools.getPath(),'../JECDatabase/textFiles/'+JEC+'_DATA/'+JEC+'_DATA')
    cfg['JsonFiles'] = [os.path.join(configtools.getPath(),'data/json/Cert_'+RUN+'_13TeV_23Sep2016ReReco_Collisions16_JSON.txt')]
    cfg['LeptonSFRootfile'] = os.path.join(configtools.getPath(),"data/scalefactors/2016all/SFDATA_GH.root")
    cfg['LeptonTriggerSFRootfile'] = os.path.join(configtools.getPath(),"data/scalefactors/2016all/SFTriggerDATA_GH.root")
    cfg['TriggerSFRuns'] = []
    return cfg
