from instascrape import *
from selenium import webdriver
from file_handler import FileHandler
import time
import sys

'''----------- CONSTANTS / FUNCTIONS -------------'''

CREATE_OPTION = "create"
APPEND_OPTION = "append"
ARGUMENT_OPTIONS = [CREATE_OPTION, APPEND_OPTION]

URLS_FILE_PATH = 'whatpantsarethose_urls.txt'
CAPTIONS_FILE_PATH = 'whatpantsarethose_captions_raw.txt'
handler = FileHandler(URLS_FILE_PATH, CAPTIONS_FILE_PATH)

# Paste chromedriver path here
DRIVER = webdriver.Chrome('/Users/reesegyllenhammer/downloads/chromedriver')

# Paste instagram sessionid here
SESSIONID = '17b327ac839-2cdd62'
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
    max_index = len(posts)
    for post in posts:
        try:
            scrape(headers=HEADERS)
        except:
            max_index = i
            break

        time.sleep(5)
        print('Successfully Scrape Post', i)
        i += 1

    print('***** SUCCESFULLY DOWNLOADED ALL POSTS UP TO {}, WRITING THEM TO FILE'.format(i))

    urls = extract_data(posts, 'url', 0, max_index)
    captions = extract_data(posts, 'caption', 0, max_index)

    handler.write_all_data(urls, captions)

def download_until_last(posts):

    # Get most recent URL downloaded
    most_recent_url = handler.get_most_recent_url()

    i = 1
    for post in posts:
        try:
            post.scrape(headers=HEADERS)
            print('Successfully Scrape Post', i)
        except:
            print('STOPPING DUE TO ERROR ON POST', i)
            break

        # Have seen the last post successfully downloaded
        if post['url'] == most_recent_url:
            if i == 1:
                raise Exception('NO NEW POSTS')

            print('New Posts', i - 1)
            break

        time.sleep(5)
        i += 1

    urls = extract_data(posts, 'url', 0, i - 1)
    captions = extract_data(posts, 'caption', 0, i - 1)
        
    handler.prepend_new_data(urls, captions)
        
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
posts = pants_profile.get_posts(DRIVER, login_first=True, login_pause=20, max_failed_scroll=1000)

if sys.argv[1] == CREATE_OPTION:
    download_all_posts(posts)
else:
    download_until_last(posts)
