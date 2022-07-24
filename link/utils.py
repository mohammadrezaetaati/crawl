import time
import requests
from io import BytesIO
from bs4 import BeautifulSoup

from django.core import files

from .models import Crawler, Images


def read_url(csv):
    with open(str(csv), "r") as f:
        lines = f.read().splitlines()
        return lines


def download_image(url, page_url):
    resp = requests.get(url)
    fp = BytesIO()
    fp.write(resp.content)
    file_name = url.split("/")[-1]
    photo: Images() = Images()
    photo.crawler = page_url
    return photo.image.save(file_name, files.File(fp))


def get_link(urls):

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:93.0)\
             Gecko/20100101 Firefox/93.0",
        "Accept-Lanquage": "utf8",
    }

    for url in urls[1:]:
        if str(url) != "None":

            start_time = time.time()
            img = []
            lnk = []
            crawler: Crawler = Crawler.objects.create(url_page=url)
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, "lxml")

            images = soup.find_all("img")
            for index_img, image in enumerate(images):
                img.append(image.get("data-src"))
                link_imge = image.get("data-src")
                if str(link_imge) != "None":
                    download_image(str(image.get("data-src")), crawler)

            links = soup.find_all("a")
            for index_ink, link in enumerate(links):
                lnk.append(link.get("href"))

            """
            save  result of crwal on database
            """
            end_time = time.time()
            time_crawl = end_time - start_time
            crawler.url = lnk
            crawler.count_img = index_img
            crawler.img = img
            crawler.count_url = index_ink
            crawler.count_img = index_img
            crawler.time_crawl = f"{time_crawl}(second)"
            crawler.save()
