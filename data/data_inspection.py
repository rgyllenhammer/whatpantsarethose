'''
FILE USED TO LOAD RAW FILES TO CHECK ANY DISCREPANCIES
RUN WITH ...
    python3 -i data_inspection.py
TO INTERACT WITH THE DATA
'''

data_urls = []
data_captions = []

with open('whatpantsarethose_urls.txt', 'r') as furls:
    data_urls = furls.readlines()

with open('whatpantsarethose_captions_raw.txt', 'r') as fcaptions:
    data_captions = fcaptions.readlines()