'''
FILE USED TO COLLECT DATA FROM INSTAGRAM.
USES INSTASCRAPE TO COLLECT DATA BUT
CAN BE DONE MANUALLY WITH SELENIUM / BS4

RUN WITH
    python3 -i data_collection.py

IN ORDER TO WRITE THE DATA TO A FILE FROM A
PYTHON INTERPRETER SINCE INSTAGRAM WILL RATE LIMIT
YOU BEFORE SCRAPING IS FINISHED
'''

from instascrape import *
from selenium import webdriver
import time

# PASTE YOUR CHROMEDRIVER PATH HERE
DRIVER = webdriver.Chrome('/path/to/chromedriver')

# PASTE YOUR SESSIONID HERE
SESSIONID = 'instagram_session_id'
HEADERS = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43",
"cookie":f'sessionid={SESSIONID};'
}

# extracts FEATURE from DATA at all indices i where START_INDEX <= i < END_INDEX
def extract_data(data, feature, start_index, end_index):
    return [data[i][feature] for i in range(start_index, end_index)]

# Instantiation
pants_profile = Profile("https://www.instagram.com/whatpantsarethose/?hl=en")
pants_profile.url = "https://www.instagram.com/whatpantsarethose/?hl=en"


# Scraping profile to load posts
PANTS_PROFILE.scrape(headers=HEADERS)

# Processing scrape data and load posts
posts = PANTS_PROFILE.get_posts(DRIVER, login_first=True, login_pause=20, max_failed_scroll=1000)

# Manually scrape posts since built in instascrape method fails
i = 1
for post in posts:
    post.scrape(headers=HEADERS)
    time.sleep(5)
    print('scraping post', i)
    i += 1


# IF DATA GATHERING FINISHES ALL OF THE WAY YOU MAY WRITE DATA LIKE THIS, IF NOT EDIT THE START AND END INDICES APPROPRIATELY
'''
with open('whatpantsarethose_captions_raw.txt', 'w') as fwritecaptions:
    urls = extract_data(posts, 'url', 0, len(posts))
    for url in urls:
        fwritecaptions.write(url)

with open('whatpantsarethose_urls.txt', 'w') as fwriteurls:
    captions = extract_data(posts, 'caption', 0, len(posts))
    for caption in captions:
        fwriteurls.write(caption)
'''

