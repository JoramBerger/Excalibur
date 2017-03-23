import configtools


def config():
	cfg = configtools.getConfig('mc', 2016, 'mm', bunchcrossing='25ns')
	cfg["InputFiles"].set_input(
#failed		ekppath="/storage/8/wayand/gc_zjets/full_lep_v5/crab_Zll_DYJetsToLL_M-50_amcatnloFXFX-pythia8_ext4_25ns/results/*.root",
#old mc@nlo
		nafpath="/pnfs/desy.de/cms/tier2/store/user/afriedel/Skimming/mcbkg_Moriond/ZZ/*.root",
	)
	cfg = configtools.expand(cfg, ['nocuts', 'zcuts', 'leptoncuts'], ['None'])
	configtools.remove_quantities(cfg, ['jet1btag', 'jet1qgtag', 'jet1rc'])
	cfg['NumberGeneratedEvents'] = 998034
	cfg['CrossSection'] = 15.6  # http://arxiv.org/pdf/1512.05314v2.pdf
	return cfg
