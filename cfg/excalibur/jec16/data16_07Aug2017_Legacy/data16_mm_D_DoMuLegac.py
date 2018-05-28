import configtools
import os

RUN='BCD'
CH='mm'
JEC='Summer16_07Aug2017'+RUN+'_V6'

#_path_prefix = "/storage/gridka-nrg"
_path_prefix = "srm://cmssrm-kit.gridka.de:8443/srm/managerv2?SFN=/pnfs/gridka.de/cms/disk-only/store/user"

def config():
    cfg = configtools.getConfig('data', 2016, CH, bunchcrossing='25ns')
    cfg["InputFiles"].set_input(
        ekppathD="{}/tberger/Skimming/ZJet_DoubleMuon_Run2016D-Legacy-07Aug2017-v1/*.root".format(_path_prefix),
        )
    cfg['Pipelines']['default']['Processors'] += ['filter:EtaPhiCleaningCut']
    cfg['CutEtaPhiCleaningFile'] = os.path.join(configtools.getPath() , 'data/cleaning/hcal-legacy-runD.root') #File used for eta-phi-cleaning, must contain a TH2D called "h2jet"
    cfg['CutEtaPhiCleaningPt'] = 15 # minimum pt for eta-phi-cleaning
    cfg['JsonFiles'] =  [os.path.join(configtools.getPath(),'data/json/Cert_'+RUN+'_13TeV_23Sep2016ReReco_Collisions16_JSON.txt')]
    cfg['Jec'] = os.path.join(configtools.getPath(),'../JECDatabase/textFiles/'+JEC+'_DATA/'+JEC+'_DATA')
    cfg['VertexSummary'] = 'offlinePrimaryVerticesSummary'
    cfg['ProvideL2ResidualCorrections'] = False
    cfg = configtools.expand(cfg, ['nocuts','basiccuts','finalcuts'], ['None', 'L1', 'L1L2L3', 'L1L2L3Res'])
	
    return cfg
