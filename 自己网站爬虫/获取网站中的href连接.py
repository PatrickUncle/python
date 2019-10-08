from os.path import join

import requests
from bs4 import BeautifulSoup
import os

base_url = "http://www.yuewct.com"

def getAllHref(url):
    href_list = []
    re = requests.get(url)
    re.encoding = "utf-8"
    soup = BeautifulSoup(re.text, "lxml")


    a_list = soup.find_all("a")
    i = 0
    for a in a_list:
        try:
            if a["href"] and a["href"] != "#" and a["href"] != "javascript:;" and a["href"] != "/":
                if i % 20 == 0:
                    print()
                print(base_url + a["href"])
                i +=1
        except:
            pass
    return href_list

if __name__ == '__main__':

    visit_href = []
    visit_href.append(base_url +"/")
    href_list = getAllHref(base_url)
    print(href_list)
    # href_list.remove(base_url + "/")
    # for url in href_list:
    #     print("当前url",url)
    #     if url in visit_href:
    #         print(url,"在列表中，执行删除，列表当前长度",len(visit_href))
    #         href_list.remove(url)
    #         continue
    #     print(href_list)
    #     href_list2 = getAllHref(url)
    #     href_list+=href_list2