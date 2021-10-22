import pandas as pd
import numpy as np
import re

def generate_dataframe():
    SKATER_REGEX = r'(@[\w|\.]+) '
    PANTS_REGEX = r'wearing (@?.+)\.'

    data_urls = []
    data_captions = []
    with open('whatpantsarethose_urls.txt', 'r') as furls:
        data_urls = furls.readlines()

    with open('whatpantsarethose_captions_raw.txt', 'r') as fcaptions:
        data_captions = fcaptions.readlines()

    return pd.DataFrame(list(zip(data_urls, data_captions)), columns=['Post Url', 'Raw Caption'])

def insert_skater(df):
    df['Skater'] = df['Raw Caption'].str.extract(SKATER_REGEX)

def insert_pant(df):
    df['Pants'] = df['Raw Caption'].str.extract(PANTS_REGEX)

def generate_csv(df):
    df.to_csv('pants_data.csv', index=False)

df = generate_dataframe()
insert_skater(df)
insert_pant(df)
generate_csv(df)
