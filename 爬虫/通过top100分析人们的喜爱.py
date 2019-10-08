import requests

from bs4 import BeautifulSoup
import json
import time

import re

times_list = []

headers = {
    'user-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
}

def get_url_list():
    url_list = []
    for i in range(1,11):
        if i == 1:
            url = "http://www.mtime.com/top/movie/top100/"
        else:
            url = "http://www.mtime.com/top/movie/top100/index-"+str(i)+".html"

        request = requests.get(url,headers=headers)
        soup = BeautifulSoup(request.text,'lxml')
        a_list = soup.find_all(name='a',attrs={'target':"_blank",'href': re.compile("http://movie.mtime.com/(\d+)/"),'class':'c_blue',})
        for a in a_list:
            url_list.append(a.get('href'))
    return url_list

# def Create_Ajax_URL(url):
#
# 	movie_id = url.split('/')[-2]
# 	t = time.strftime("%Y%m%d%H%M%S0368", time.localtime())
# 	ajax_url = "http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=%s&t=%s&Ajax_CallBackArgument0=%s" % (url,t,movie_id)
# 	return ajax_url


def get_want(url):
    request = requests.get(url,headers=headers)
    if request.status_code == 200:
        request.encoding='utf-8'
        soup = BeautifulSoup(request.text,'lxml')
        a_list = soup.find_all(name='a',attrs={'target' : '_blank','property' : "v:genre"})
        for a in a_list:
            if a.text not in times_list:
                times_list.append(a.text)
                times_list.append(1)
        else:
            times_list[times_list.index(a.text)+1] += 1
    return times_list


def main():
    for url in get_url_list():
        get_want(url)
    print(times_list)

if __name__ == '__main__':
    main()
