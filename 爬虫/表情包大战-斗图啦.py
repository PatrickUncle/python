import os
import urllib.request
import requests
from bs4 import BeautifulSoup
import threading

imgMasage_list =[]
gLock = threading.Lock()

#生成全部页面url_list
url_list = []
for x in range(1,1509):
    url = "https://www.doutula.com/photo/list/?page=%d"%x
    url_list.append(url)

#获取页面text
def getText(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    return req.text

#根据text获取全部的img_list
def getImg(text):
    soul = BeautifulSoup(text,"html.parser")
    img_list = soul.find_all("img",class_="img-responsive lazy image_dta")
    return img_list
#获取img_url和alt名字，并将图片名字更改好，存入全局变量的列表中
def saveMasage():
    while 1:
        if url_list == None:
            break
        url = url_list.pop()
        text = getText(url)
        img_list = getImg(text)
        for img in img_list:
            masage ={
                "img_url":img["data-original"],
                "img_name":img["alt"]
            }
            gLock.acquire()
            imgMasage_list.append(masage)
            gLock.release()

#通过全局变量下载图片
def download():
    while 1:
        gLock.acquire()
        if len(imgMasage_list) == 0:
            gLock.release()
            continue
        else:
            masage = imgMasage_list.pop()
            gLock.release()
            url = masage["img_url"]
            name = masage["img_name"]
            if name == "":
                continue
            one_list = url.split("/")
            houzhuiming = one_list.pop().split(".").pop()
            path = os.path.join("E:\images\\"+name + "."+houzhuiming)
            urllib.request.urlretrieve(url,filename=path)
            print(path + "已经下载完成...........")

#定义获取资料线程
def getMasage_Thead():
    for x in range(5):
        t = threading.Thread(target=saveMasage)
        t.start()
#定义下载资料线程
def download_Thread():
    for x in range(30):
        t = threading.Thread(target=download)
        t.start()

def main():
    getMasage_Thead()
    download_Thread()

if __name__ == '__main__':
    main()