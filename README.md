# Whatpantsarethose

A website of the instagram @whatpantsarethose to enable easy searching of both skaters and pants. Until site is hosted directly on this github the current version is over at https://rgyllenhammer.github.io/whatpantsarethose.html

# Requirements

- Pandas
- Numpy
- Instascrape
  - Install with `pip3 install insta-scrape`

# Workflow
The current workflow follows as this. Data is downloaded somehow in this file: https://github.com/rgyllenhammer/whatpantsarethose/blob/main/data/data_collection.py where you decide to attempt to download the whole instagram worth of data, or just append new posts that have been posted since last collection. That data is written to two files where it is then processed by this file: https://github.com/rgyllenhammer/whatpantsarethose/blob/main/data/data_processing.py which transforms the data, creates a dataframe, and writes data to an html file to display

# Future work

- Move site to hosting service that can hold a real backend
- Search by both skater and pant
- Automatically update with new posts
