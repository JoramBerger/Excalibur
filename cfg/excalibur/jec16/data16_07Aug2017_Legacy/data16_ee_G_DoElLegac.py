import configtools
import os

RUN='G'
CH='ee'
JEC='Summer16_07Aug2017'+RUN+'_V6'

#_path_prefix = "/storage/gridka-nrg"
#_path_prefix = "srm://cmssrm-kit.gridka.de:8443/srm/managerv2?SFN=/pnfs/gridka.de/cms/disk-only/store/user"
_path_prefix = "root://cmsxrootd-1.gridka.de:1094///store/user"

def config():
    cfg = configtools.getConfig('data', 2016, CH, bunchcrossing='25ns')
    cfg["InputFiles"].set_input(
        ekppathF="{}/tberger/Skimming/ZJet_DoubleElectron_Run2016F-Legacy-07Aug2017-v1/*.root".format(_path_prefix),
        ekppathG="{}/tberger/Skimming/ZJet_DoubleElectron_Run2016G-Legacy-07Aug2017-v1/*.root".format(_path_prefix),
        )
    cfg['JsonFiles'] =  [os.path.join(configtools.getPath(),'data/json/Cert_'+RUN+'_13TeV_23Sep2016ReReco_Collisions16_JSON.txt')]
    cfg['Jec'] = os.path.join(configtools.getPath(),'../JECDatabase/textFiles/'+JEC+'_DATA/'+JEC+'_DATA')
    cfg['VertexSummary'] = 'offlinePrimaryVerticesSummary'
    cfg['ProvideL2ResidualCorrections'] = False
    cfg = configtools.expand(cfg, ['nocuts','basiccuts','finalcuts'], ['None', 'L1', 'L1L2L3', 'L1L2L3Res'])

    return cfg
