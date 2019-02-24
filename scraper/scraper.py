import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base_url = "http://apod.nasa.gov/apod/archivepix.html"
download_directory = "apod_pix"
content = urllib.request.urlopen(base_url).read()

for link in BeautifulSoup(content, "lxml").findAll("a"):
    print ("following link:", link)
    href = urljoin(base_url, link["href"])
    content = urllib.request.urlopen(href).read() 
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(href, img["src"])
        print("Downloading image: ", img_href)
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))





