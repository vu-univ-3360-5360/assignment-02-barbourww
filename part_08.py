# WILLIAM BARBOUR
# UNIV 5360
# ASSIGNMENT 1: PYTHON
# 01/22/2018

# PART 8
# WRAP UP AND NEXT STEPS
# ---------------------------------------------------------------

# Import the datadotworld module as dw and the sys module
import datadotworld as dw
import sys

# Import a dataset
refugee_dataset = dw.load_dataset('nrippner/refugee-host-nations')

# Get the size of the dataset:
sys.getsizeof(refugee_dataset)

# List all of the data files:
dataframes = refugee_dataset.dataframes
for df in dataframes:
    pp.pprint(df)
    
# print all of the files in a dataset:
resources = refugee_dataset.describe()['resources']
pp.pprint('name:')
for r in resources:
    pp.pprint(r['name'])
pp.pprint('\ntype of file:')
for r in resources:
    pp.pprint(r['format'])

