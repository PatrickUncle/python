# _*_ utf-8 _*_
from bs4 import BeautifulSoup
import requests
import urllib.request
import os
HOST = r"http://www.yuewct.com"
web_url = r"http://www.yuewct.com/search/?csrfmiddlewaretoken=ZLN4hSOHeLIvW5pgWuyAvfXtoAU8OTHh6SwpWILoH7eBY5UmAZ1GUvx0zXKOlCfy&kw="
BASE_PATH = r"F:\书籍封面图片"

def GetImgURL(soup):
    div_cover = soup.find_all("div",attrs={"class":"book_cover"})
    img_url = []
    for div in div_cover:
        url = HOST + div.find("img")["src"]
        img_url.append(url)
    return img_url

def download(url):
    filename = url.split("/")[-1]
    print(url)
    try:
        urllib.request.urlretrieve(url, os.path.join(BASE_PATH,filename))
    except:
        download(url)


if __name__ == '__main__':
    re = requests.get(web_url)
    re.encoding = "utf-8"
    soup = BeautifulSoup(re.text, "lxml")
    img_list = GetImgURL(soup)
    for url in img_list:
        download(url)
