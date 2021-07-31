import pandas as pd
import numpy as np
import re

SKATER_REGEX = r'(@[\w|\.]+) '
PANTS_REGEX = r'wearing (@?.+)\.'
HTML_HEADER = '<html><head><link rel="stylesheet" href="main.css"></head></body><div class="header"><h1> whatpantsarethose </h1><p>created by @ranchgod</p><p>data from @whatpantsarethose</p></div>'
HTML_FOOTER = '</body></html>'

data_urls = []
data_captions = []
with open('whatpantsarethose_urls.txt', 'r') as furls:
    data_urls = furls.readlines()

with open('whatpantsarethose_captions_raw.txt', 'r') as fcaptions:
    data_captions = fcaptions.readlines()

df = pd.DataFrame(list(zip(data_urls, data_captions)), columns=['Post Url', 'Raw Caption'])

def insert_skater(df):
    df['Skater'] = df['Raw Caption'].str.extract(SKATER_REGEX)

def insert_pant(df):
    df['Pants'] = df['Raw Caption'].str.extract(PANTS_REGEX)

def generate_skater_dictionary(df):
    skater_dictionary = {}
    for index, row in df.iterrows():
        skater = row['Skater']
        pants = row['Pants']
        url = row['Post Url']

        if skater not in skater_dictionary:
            skater_dictionary[skater] = [{'Post Url': url, 'Pants': pants}]
        else:
            skater_dictionary[skater].append({'Post Url': url, 'Pants':pants})
    return skater_dictionary

def generate_html(skater_dictionary):
    with open('../website/whatpantsarethose.html', 'r+') as htmlhandler:
        htmlhandler.write(HTML_HEADER)

        for skater in skater_dictionary:
            htmlhandler.write('<h2> {} ({} hits)</h2>'.format(skater, len(skater_dictionary[skater])))
            for data_dictionary in skater_dictionary[skater]:
                htmlhandler.write('<p>{} <a href="{}"> {} </a></p>'.format(data_dictionary['Pants'], data_dictionary['Post Url'], data_dictionary['Post Url']))

        htmlhandler.write(HTML_FOOTER)

insert_skater(df)
insert_pant(df)

generate_html(generate_skater_dictionary(df))
