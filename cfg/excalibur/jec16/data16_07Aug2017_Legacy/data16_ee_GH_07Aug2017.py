import configtools
import os
import sys

# -- import common information
sys.path.append(os.path.dirname(__file__))
from common import JEC_BASE, JEC_VERSION, SE_PATH_PREFIX

RUN='GH'
CH='ee'
JEC='{}{}_{}'.format(JEC_BASE, RUN, JEC_VERSION)


def config():
    cfg = configtools.getConfig('data', 2016, CH, JEC=JEC, IOV=RUN)
    cfg["InputFiles"].set_input(
        bmspathF="{}/dsavoiu/Skimming/ZJet_DoubleEG_Run2016F-Legacy-07Aug2017-v1_egmSSbackport/*.root".format(SE_PATH_PREFIX),
        bmspathG="{}/dsavoiu/Skimming/ZJet_DoubleEG_Run2016G-Legacy-07Aug2017-v1_egmSSbackport/*.root".format(SE_PATH_PREFIX),
        bmspathH="{}/dsavoiu/Skimming/ZJet_DoubleEG_Run2016H-Legacy-07Aug2017-v1_egmSSbackport/*.root".format(SE_PATH_PREFIX),
        ekppathF="{}/dsavoiu/Skimming/ZJet_DoubleEG_Run2016F-Legacy-07Aug2017-v1_egmSSbackport/*.root".format(SE_PATH_PREFIX),
        ekppathG="{}/dsavoiu/Skimming/ZJet_DoubleEG_Run2016G-Legacy-07Aug2017-v1_egmSSbackport/*.root".format(SE_PATH_PREFIX),
        ekppathH="{}/dsavoiu/Skimming/ZJet_DoubleEG_Run2016H-Legacy-07Aug2017-v1_egmSSbackport/*.root".format(SE_PATH_PREFIX),
        )
    cfg['JsonFiles'] =  [os.path.join(configtools.getPath(),'data/json/Cert_{}_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'.format(RUN))]

    cfg['ProvideL2ResidualCorrections'] = True
    cfg = configtools.expand(cfg, ['nocuts', 'basiccuts', 'finalcuts'], ['None', 'L1', 'L1L2L3', 'L1L2Res', 'L1L2L3Res'])

    return cfg
