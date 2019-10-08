import requests

from bs4 import BeautifulSoup
import json
import time

import re

file = open(file=r'C:\Users\ASUSPC\Desktop\时光电影.txt',mode='a',encoding='utf-8')

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

def Create_Ajax_URL(url):

	movie_id = url.split('/')[-2]
	t = time.strftime("%Y%m%d%H%M%S0368", time.localtime())
	ajax_url = "http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=%s&t=%s&Ajax_CallBackArgument0=%s" % (url,t,movie_id)
	return ajax_url


def get_want(url):
    request = requests.get(url,headers=headers)
    if request.status_code == 200:
        request.encoding='utf-8'
        result = re.findall(r'=(.*?);',request.text)[0]
        if result is not None:
            value = json.loads(result)
            value = value.get('value')
            movie_name = value.get('movieTitle')
            top_list_name = value.get('topList').get('TopListName')
            ranking = value.get('topList').get('Ranking')
            zonghe = value.get('movieRating').get('RatingFinal')
            daoyan = value.get('movieRating').get('RDirectorFinal')
            gushi = value.get('movieRating').get('RStoryFinal')
            yinyue = value.get('movieRating').get('ROtherFinal')
            huamian = value.get('movieRating').get('RPictureFinal')
            print(movie_name)
            if value.get("boxOffice"):
                qian = value.get("boxOffice").get('TotalBoxOffice')
                danwei = value.get("boxOffice").get('TotalBoxOfficeUnit')
                print("票房：%s %s"%(qian,danwei))
            print("%s——No.%s"%(top_list_name,ranking))
            print("综合评分：%s 导演评分：%s  故事评分：%s  音乐评分：%s  画面评分：%s"%(zonghe,daoyan,gushi,yinyue,huamian))
            print("****"*20)
            file.write(movie_name+"\n"+"%s——No.%s"%(top_list_name,ranking)+"\n"+"综合评分：%s 导演评分：%s  故事评分：%s  音乐评分：%s  画面评分：%s"%(zonghe,daoyan,gushi,yinyue,huamian) +"\n" +"****"*20 +"\n")





def main():
    for url in get_url_list():
        get_want(Create_Ajax_URL(url))

if __name__ == '__main__':
    main()
