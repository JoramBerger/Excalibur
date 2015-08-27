import configtools
import mc_ee

def config():
	cfg = mc_ee.config()
	cfg["InputFiles"] = configtools.setInputFiles(
		ekppath="/storage/a/dhaitz/skims/2015-07-28_ee-mc_Run2012/kappa_DYToEE*.root",
		nafpath="/pnfs/desy.de/cms/tier2/store/user/dhaitz/2015-07-28_ee-mc_Run2012/kappa_DYToEE*.root",
	)
	cfg['CrossSection'] = 1966.7
	cfg['NumberGeneratedEvents'] = 3297045
	return cfg