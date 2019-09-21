#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas
from zipfile import ZipFile

# Read in the file urls and metadata.
files = pandas.read_csv('fec_files.txt', sep='\t')
description_files = pandas.read_csv('fec_file_data_descriptions.txt', sep='\t')

# Get the data descriptions and save them in a dict as pandas dfs.
data_descriptions = {}
for index, row in description_files.iterrows():
    data_descriptions[row['data_type']] = pandas.read_html(row['file_url'], header=0)[0]

# Combine data across years for the data download categories.
data_types = set(files['data_type'])

for dt in data_types:
    # Get the files of this data type.
    this_dt = files[files['data_type'] == dt]
    # Read in each data file, unzip it, add year labels, and combine it.
    for index, row in this_dt.iterrows():
        if index == 0:
            all_years = pandas.read_csv(
                row['file_url'], sep='|', header=None, names=data_descriptions[dt]['Column name']
            ).assign(time_period=row['time_period'])
        else:
            df = pandas.read_csv(
                row['file_url'], sep='|', header=None, names=data_descriptions[dt]['Column name']
            ).assign(time_period=row['time_period'])
            all_years = pandas.concat([all_years, df], ignore_index=True)
    # At this point, you would be able to put all_years into a database with the appropriate structure.
    # You will want to add the data type (dt) as a label.

# Define where the FEC data is located.
FEC_BULK_DATA_URL = 'https://www.fec.gov/data/browse-data/'

FEC_HTML = urlopen(FEC_BULK_DATA_URL)
FEC_BS = BeautifulSoup(FEC_HTML.read()) # BeautifulSoup parsed object.


# Original plan for this script:

# Get the bulk data download tab from the html.

# This turned out to be pretty difficult, because there wasn't a single html
# class, attribute, id, or anything that identified all of the data download
# sections.


# Get the description of each section.

# Get the list of files for each section, along with time period label.

# Get the url for the data dictionary.

# Get each file, unzip it, and extract the contents.

# Get the contents of the data dictionary. (pandas read_html)

