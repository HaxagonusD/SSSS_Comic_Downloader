from bs4 import BeautifulSoup
import requests
import urllib.request
from pathlib import Path


# r = requests.get('http://www.sssscomic.com/?id=archive')

# ssss_soup = BeautifulSoup(r.text, 'html.parser')


def download_everyting():
    r = requests.get('http://www.sssscomic.com/?id=archive')
    ssss_soup = BeautifulSoup(r.text, 'html.parser')
    last_page_link = ssss_soup('a')[-1]
    how_many_pages = int(last_page_link.text)

    for page_number in range(1, how_many_pages+1):
        page = requests.get(
            'http://www.sssscomic.com/comic.php?page=' + str(page_number))
        soup = BeautifulSoup(page.text, 'html.parser')
        image = soup('img', class_='comicnormal')[0]
        image_source = image['src']
        Path(image_source).touch()
        urllib.request.urlretrieve(
            "http://sssscomic.com/"+image_source, image_source)
        print("Downloaded: " + image_source)


download_everyting()
