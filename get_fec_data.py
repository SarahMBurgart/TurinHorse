#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen


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

