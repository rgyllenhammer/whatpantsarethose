'''
FILE USED TO COLLECT DATA FROM INSTAGRAM.
USES INSTASCRAPE TO COLLECT DATA BUT
CAN BE DONE MANUALLY WITH SELENIUM / BS4

RUN WITH
    python3 -i data_collection.py create
IN ORDER TO CREATE THE WHOLE DATASET FROM SCRATCH

RUN WITH
    python3 -i data_collection.py append
IN ORDER TO CAPTURE THE MOST RECENT POSTS

MUST BE RAN IN -i MODE BECAUSE INSTAGRAM MAY RATE LIMIT
IN WHICH CASE DATA MUST BE WRITTEN TO FILE MANUALLY.
'''

from instascrape import *
from selenium import webdriver
import time
import sys

'''----------- CONSTANTS / FUNCTIONS -------------'''

CREATE_OPTION = "create"
APPEND_OPTION = "append"
ARGUMENT_OPTIONS = [CREATE_OPTION, APPEND_OPTION]

# Paste chromedriver path here
DRIVER = webdriver.Chrome('/path/to/chromedriver')

# Paste instagram sessionid here
SESSIONID = 'instagram_session_id'
HEADERS = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
"cookie":f'sessionid={SESSIONID};'
}

# Extracts FEATURE from DATA at all indices i where START_INDEX <= i < END_INDEX
def extract_data(data, feature, start_index, end_index):
    return [data[i][feature] for i in range(start_index, end_index)]

# Scrapes all of POSTS until instagram rate limits us or it finishes
def download_all_posts(posts):
    i = 1
    for post in posts:
        post.scrape(headers=HEADERS)
        time.sleep(5)
        print('Successfully Scrape Post', i)
        i += 1

    print('***** SUCCESFULLY DOWNLOADED ALL POSTS, WRITING THEM TO FILE')

    with open('whatpantsarethose_captions_raw.txt', 'w') as fwritecaptions:
    urls = extract_data(posts, 'url', 0, len(posts))
    for url in urls:
        fwritecaptions.write(url)

    with open('whatpantsarethose_urls.txt', 'w') as fwriteurls:
        captions = extract_data(posts, 'caption', 0, len(posts))
        for caption in captions:
            fwriteurls.write(caption)


def download_until_last(posts):

    # Get most recent URL downloaded
    with open('whatpantsarethose_urls.txt', 'r') as urlreader:
        url_content = urlreader.read()
        most_recent_url = url_content.splitlines()[0].strip()

    i = 1
    for post in posts:
        post.scrape(headers=HEADERS)
        print('Successfully Scrape Post', i)

        # Have seen the last post successfully downloaded
        if post['url'] == most_recent_url:
            print('New Posts', i)
            break

        time.sleep(5)
        i += 1

    urls = extract_data(posts, 'url', 0, i)
    captions = extract_data(posts, 'caption', 0, i)
        
    # May open in write since we have already read the URL content above
    with open('whatpantsarethose_urls.txt', 'w') as urlhandler:
        urhandler.seek(0,0)

        for url in urls:
            urlhandler.write(url + '\n')

        urlhandler.write(url_content)

    # Must open file as read and write because we have not yet read the contents to be able to insert into the front
    with open('whatpantsarethose_captions_raw.txt', 'r+') as captionhandler:
        caption_content = captionhandler.read()
        captionhandler.seek(0, 0)

        for caption in captions:
            captionhandler.write(caption + '\n')

        captionhandler.write(caption_content)
        
'''----------- CONSTANTS / FUNCTIONS -------------'''

# Check if argument is passed in and formatted correctly
if (len(sys.argv) != 2 or sys.argv[1] not in ARGUMENT_OPTIONS):
    raise Exception('ERROR NOT ENOUGH ARGUMENTS')

# Instantiation
pants_profile = Profile("https://www.instagram.com/whatpantsarethose/?hl=en")
pants_profile.url = "https://www.instagram.com/whatpantsarethose/?hl=en"

# Scraping profile to load posts
pants_profile.scrape(headers=HEADERS)

# Processing scrape data and load posts
posts = PANTS_PROFILE.get_posts(DRIVER, login_first=True, login_pause=20, max_failed_scroll=1000)

if sys.argv[1] == CREATE_OPTION:
    download_all_posts(posts)
else:
    download_until_last(posts)
