import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urlparse


class url:
    def __init__(self, url):
        # Initialize the url object with a URL
        self.url = url

    def get_url(self):
        # Return the current URL
        return self.url

    def set_url(self, url):
        # Set a new URL
        self.url = url

    def get_html(self, auth=None):
        # Fetch the HTML content of the URL, with optional authentication
        if auth:
            results = requests.get(self.url, auth=auth)
        else:
            results = requests.get(self.url)
        return results

    def get_soup(self, auth=None):
        # Parse the HTML content using BeautifulSoup and return the soup object
        return BeautifulSoup(self.get_html(auth=auth).text, "html.parser")

    def get_links(self, auth=None):
        # Extract and return all hyperlinks from the HTML content
        soup = self.get_soup(auth=auth)
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links

    def get_images(self, auth=None):
        # Extract and return all image sources from the HTML content
        soup = self.get_soup(auth=auth)
        images = []
        for img in soup.find_all('img'):
            images.append(img.get('src'))
        return images

    def get_title(self, auth=None):
        # Extract and return the title of the HTML content
        soup = self.get_soup(auth=auth)
        return soup.title.string

    def get_text(self, auth=None):
        # Extract and return all text content from the HTML content
        soup = self.get_soup(auth=auth)
        return soup.get_text()

    def get_meta(self, auth=None):
        # Extract and return all meta tag contents from the HTML content
        soup = self.get_soup(auth=auth)
        meta = []
        for tag in soup.find_all('meta'):
            meta.append(tag.get('content'))
        return meta

    def get_links_count(self, auth=None):
        # Return the count of hyperlinks in the HTML content
        return len(self.get_links(auth=auth))

    def get_images_count(self, auth=None):
        # Return the count of images in the HTML content
        return len(self.get_images(auth=auth))

    def get_meta_count(self, auth=None):
        # Return the count of meta tags in the HTML content
        return len(self.get_meta(auth=auth))

    def get_text_count(self, auth=None):
        # Return the count of text elements in the HTML content
        return len(self.get_text(auth=auth))

    def get_title_count(self, auth=None):
        # Return the count of title elements in the HTML content
        return len(self.get_title(auth=auth))

    def get_all(self, auth=None):
        # Return a dictionary with all extracted elements and their counts
        return {
            "url": self.url,
            "title": self.get_title(auth=auth),
            "links": self.get_links(auth=auth),
            "images": self.get_images(auth=auth),
            "meta": self.get_meta(auth=auth),
            "text": self.get_text(auth=auth),
            "links_count": self.get_links_count(auth=auth),
            "images_count": self.get_images_count(auth=auth),
            "meta_count": self.get_meta_count(auth=auth),
            "text_count": self.get_text_count(auth=auth),
            "title_count": self.get_title_count(auth=auth)
        }

    def clear(self):
        # Clear the URL attribute
        self.url = None
        

class UrlManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.to_process = deque()
        self.processed = set()

    def is_native(self, url):
        base_domain = urlparse(self.base_url).netloc
        url_domain = urlparse(url).netloc
        return base_domain == url_domain

    def add_url(self, url):
        normalized_url = url.rstrip('/')
        if self.is_native(normalized_url) and normalized_url not in self.processed and normalized_url not in self.to_process:
            self.to_process.append(normalized_url)

    def add_urls(self, urls):
        for url in urls:
            self.add_url(url)

    def get_next_url(self):
        if self.to_process:
            next_url = self.to_process.popleft()
            self.processed.add(next_url)
            return next_url
        return None

    def has_urls_to_process(self):
        return len(self.to_process) > 0
    
    def urls_to_process_count(self):
        return f'{len(self.to_process)} URLs left to process'