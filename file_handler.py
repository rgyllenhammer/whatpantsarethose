# class specifically used for writing to and from url and caption files

class FileHandler:
    def __init__(self, urls_file_path, captions_file_path):
        self.URLS_FILE_PATH = urls_file_path
        self.CAPTIONS_FILE_PATH = captions_file_path

    def write_all_data(self, urls, captions):
        with open(self.CAPTIONS_FILE_PATH, 'w') as fwritecaptions:
            for url in urls:
                fwritecaptions.write(url)

        with open(self.URLS_FILE_PATH, 'w') as fwriteurls:
            for caption in captions:
                fwriteurls.write(caption)

    def prepend_new_data(self, urls, captions):
        with open(self.URLS_FILE_PATH, 'r+') as urlhandler:
        url_content = urlhandler.read()
        urlhandler.seek(0,0)

        for url in urls:
            urlhandler.write(url + '\n')

        urlhandler.write(url_content)

        with open(self.CAPTIONS_FILE_PATH, 'r+') as captionhandler:
            caption_content = captionhandler.read()
            captionhandler.seek(0, 0)

            for caption in captions:
                captionhandler.write(caption + '\n')

            captionhandler.write(caption_content)
        
    def get_most_recent_url(self):
         with open(self.URLS_FILE_PATH, 'r') as urlreader:
            url_content = urlreader.read()
            most_recent_url = url_content.splitlines()[0].strip()

            return most_recent_url