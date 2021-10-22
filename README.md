# Whatpantsarethose

A website of the instagram @whatpantsarethose to enable easy searching of both skaters and pants. Until site is hosted directly on this github the current version is over at https://rgyllenhammer.github.io/whatpantsarethose.html

# Requirements

- Pandas
- Numpy
- Instascrape
  - Install with `pip3 install insta-scrape`

# Workflow
The current workflow follows as this. Data is downloaded somehow in this file: https://github.com/rgyllenhammer/whatpantsarethose/blob/main/data/data_collection.py where you either download the whole instagrams worth of data, or just append new posts that have been posted since last collection. That data is written to two files where it is then processed by this file: https://github.com/rgyllenhammer/whatpantsarethose/blob/main/data/data_processing.py which transforms the data, creates a dataframe, and writes it to a csv

# Website
There is now a node site that hosts this data at https://github.com/rgyllenhammer/whatpantsarethose_site. This website will also eventually have an API so that it is not necessary for you to download data using this method. Perhaps eventually this method will be irrelevant, as data is moved to MongoDB
