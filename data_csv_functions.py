#!/usr/bin/env python2
import pandas as pd

def import_from_csv(file_name):
	print('=' * 60)
	print("Loading file: %s" % str(file_name))
	dataset=pd.read_csv(file_name, sep='\t')
	print("Loading finished.")
	print('=' * 60)
	return dataset

def export_to_csv(file_name,data):
	print('=' * 60)
	print("Exporting to file: %s" % str(file_name))
	dataset = pd.DataFrame.from_dict(data, orient='index')
	dataset.to_csv(file_name, sep='\t', na_rep='0.00', encoding='utf-8', dialect='excel')
	print("Exporting finished.")
	print('=' * 60)
	return