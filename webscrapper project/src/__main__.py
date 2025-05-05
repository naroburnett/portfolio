import requests
# from requests import get
# from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np
import re
from pathlib import Path
from datetime import datetime
# import xml.etree.ElementTree as ET
from classes import url, UrlManager

url_test = "https://stagingultraluxhealth.com"
auth_test = ("spartacus", "ThisIsSparta!234")
main_folder_test = "ultraLux Health Test"
output_folder_test = "outputLogScrapper"


def main():
    while True:
        print("Main Menu")
        print("1. Scrape HTML")
        print("2. Single Page HTML Scrapper")
        print("3. Test")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            htmlScrapper()
            input("Press Enter to continue...")
        elif choice == '2':
            singlePageHtmlScrapper()
            input("Press Enter to continue...")
        elif choice == '3':
            test_url_class()
            input("Press Enter to continue...")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def htmlScrapper():
    # Prompt the user for the starting URL ****
    start_url = input("Enter the starting URL: ")

    # Attempt to access the URL without authentication
    response = requests.get(start_url)
    
    # Check if authentication is required
    if response.status_code == 401:
        print("Authentication is required.")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        auth = (username, password)
    else:
        auth = None

    # Create an instance of the url class with the provided URL and authentication
    webpage = url(start_url)
    soup = webpage.get_soup(auth=auth)

    # Check if the output directory exists
    output_dir = Path("Output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Prompt the user for a title
    user_title = "UltraLux Health" # input("Enter a title for the folder: ")
    user_dir = output_dir / user_title
    user_dir.mkdir(parents=True, exist_ok=True)

    # Create "HTML Files" directory inside the user directory
    html_files_dir = user_dir / "HTML Files"
    html_files_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename with the title of the URL and current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    url_title = webpage.get_title(auth=auth) #start_url.replace("https://", "").replace("http://", "").replace("/", "_")
    filename = html_files_dir / f"{url_title}_{current_time}.html" #day vs entire time

    with filename.open("w", encoding="utf-8") as file:
        file.write(soup.prettify())
    
    print("Successfully Set up Inital Scrap and documented Starting Page")
    print("Please check the Output Folder for the HTML file and validate the content")
    print("If the content is correct, please proceed to the next step")
    input("Press Enter to continue...")
    print("Beginning to scrape the site")

    # Create an instance of UrlManager
    foreman = UrlManager(webpage.get_url())

    # Add the starting URL to the list
    foreman.add_url(webpage.get_url())

    #print(foreman.urls_to_process_count())

    # Process the URLs
    max_urls_to_process = int(10)  # Limit the number of URLs to process for testing purposes
    processed_count = int(0)

    while foreman.has_urls_to_process() and (processed_count < max_urls_to_process):
        current_url = foreman.get_next_url()
        webpage = url(current_url)
        soup = webpage.get_soup(auth=auth)

        # Generate filename with the title of the URL and current date and time
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        url_title = webpage.get_title(auth=auth) #current_url.replace("https://", "").replace("http://", "").replace("/", "_")
        filename = html_files_dir / f"{url_title}_{current_time}.html"

        with filename.open("w", encoding="utf-8") as file:
            file.write(soup.prettify())

        print(f"Successfully scraped {current_url} and saved the HTML content to {filename}")

        # Get all native hyperlinks from the HTML
        links = [a['href'] for a in soup.find_all('a', href=True) if foreman.is_native(a['href'])]

        # Add the hyperlinks to the UrlManager
        foreman.add_urls(links)

        webpage.clear()
        processed_count += 1

def test_url_class():
     # Prompt the user to enter the URL
    url_input = input("Enter the URL: ")
    
    # Attempt to access the URL without authentication
    webpage = url(url_input)
    response = webpage.get_html()
    
    # Check if authentication is required
    if response.status_code == 401:
        print("Authentication is required.")
        # username = input("Enter the username: ")
        # password = input("Enter the password: ")
        # auth = (username, password)
        auth = ('spartacus', 'ThisIsSparta!234')
    print("Webpage Link Count:")
    print(webpage.get_links_count(auth=auth))
    print("Webpage Links:")
    print(webpage.get_links(auth=auth))

    return

def singlePageHtmlScrapper():
    # Prompt the user for the URL
    url_input = input("Enter the URL: ")

    # Attempt to access the URL without authentication
    response = requests.get(url_input)
    
    # Check if authentication is required
    if response.status_code == 401:
        print("Authentication is required.")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        auth = (username, password)
    else:
        auth = None

    # Create an instance of the url class with the provided URL and authentication
    webpage = url(url_input)
    soup = webpage.get_soup(auth=auth)

    # Check if the output directory exists
    output_dir = Path("Output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Prompt the user for a title
    user_title = input("Enter a title for the folder: ")
    user_dir = output_dir / user_title
    user_dir.mkdir(parents=True, exist_ok=True)

    # Create "HTML Files" directory inside the user directory
    html_files_dir = user_dir / "HTML Files"
    html_files_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename with the title of the URL and current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    url_title = webpage.get_title(auth=auth)
    # Sanitize the url_title to remove invalid characters
    url_title = re.sub(r'[<>:"/\\|?*]', '_', url_title)
    filename = html_files_dir / f"{url_title}_{current_time}.html"

    with filename.open("w", encoding="utf-8") as file:
        file.write(soup.prettify())

    print(f"Successfully scraped {url_input} and saved the HTML content to {filename}")


if __name__ == "__main__":
    main()
