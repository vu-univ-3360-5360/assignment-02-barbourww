# WILLIAM BARBOUR
# UNIV 5360
# ASSIGNMENT 1: PYTHON
# 01/22/2018


# PART 3
# METADATA
# ---------------------------------------------------------------

# 5 data fields


# ACCESSING DATA
# ---------------------------------------------------------------

# The datadotworld module and dataset have already been loaded for you:
import datadotworld as dw
dataset = dw.load_dataset('https://data.world/stephen-hoover/chicago-city-council-votes')

# Use the dataframes property to assign the alderman_votes table to the variable votes_dataframe.
votes_dataframe = dataset.dataframes['alderman_votes']

# Use the pandas shape property to get rows/columns size for the `votes_dataframe` dataframe.
pp.pprint(votes_dataframe.shape)

# Use the pandas head function to print the first 3 rows of the `votes_dataframe` dataframe.
pp.pprint(votes_dataframe.head(3))