import ZJetConfigBase as base
import ZJetWrapper


def config():
    cfg = base.getConfig('mc', 2012, 'mm')
    cfg["InputFiles"] = base.setInputFiles(
        #ekppath="root://cms-xrd-global.cern.ch//store/user/tmuller/higgs-kit/skimming/2014-07-30-full_skim/DYJetsToLL_M_50_madgraph_8TeV/kappa_DYJetsToLL_M_50_madgraph_8TeV_1000.root",
        ekppath="/storage/6/berger/kappatest/skim_kappa2_data.root",
        nafpath=""
    )
    cfg = base.expand(cfg, ['all', 'zcuts', 'incut'])
    return cfg