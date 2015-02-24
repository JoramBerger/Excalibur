# -*- coding: utf-8 -*-

import argparse

import logging
import Artus.Utility.logger as logger
log = logging.getLogger(__name__)

import Excalibur.Plotting.harryZJet as harryZJet


def plotscript(dicts):
	""" main """	
	# get max processes name from command line
	parser = argparse.ArgumentParser()
	parser.add_argument('--max-processes', type=int, default=8)
	opt, unknown_args = parser.parse_known_args()

	log.info("Doing {} plots".format(len(dicts)))

	harry_instance = harryZJet.HarryPlotterZJet(
		list_of_config_dicts=dicts,
		list_of_args_strings=" ".join(unknown_args),
		n_processes=min(opt.max_processes, len(dicts))
	)
