import pandas as pd
import json
from pandas.io.json import json_normalize
import numpy as np

# define json string
data = [{'state': 'Florida', 
         'shortname': 'FL',
         'info': {'governor': 'Rick Scott'},
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {'governor': 'John Kasich'},
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]

# use normalization to create tables from nested element
json_normalize(data, 'counties')

# further populate tables created from nested element
json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])

# load json as string
json.load((open('data/world_bank_projects_less.json')))

# load as Pandas dataframe
sample_json_df = pd.read_json('data/world_bank_projects_less.json')
sample_json_df

# load json as string
json.load((open('data/world_bank_projects.json')))
# load as Pandas dataframe
world_bank_projects_df = pd.read_json('data/world_bank_projects.json')
country_frequencies = world_bank_projects_df['countryshortname'].value_counts()
print(country_frequencies[0:10])

# Extract the column from the data frame
mjtheme_column = world_bank_projects_df['mjtheme_namecode']

# Create a list of the dictionaries from the column
major_themes = [mjtheme_column[j][k] for j in range(len(mjtheme_column)) for k in range(len(mjtheme_column[j]))]

# Convert the list of dictionaries to data frame
major_themes_df = pd.DataFrame(major_themes)
print(major_themes_df)
major_themes_frequencies = major_themes_df['name'].value_counts(dropna=True)
print(major_themes_frequencies)


major_theme_grouping_df = major_themes_df.groupby('name').describe()
temp = major_theme_grouping_df['code']['top']
code_name_pair = {temp[i]:temp.index[i] for i in range(len(temp))}
print(code_name_pair)

print(major_themes_df.isna())
