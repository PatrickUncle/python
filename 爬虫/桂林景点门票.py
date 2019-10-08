import requests
from bs4 import BeautifulSoup


def getHtml(url):
    rqs = requests.get(url)
    #切换编码方式 与网页本身使用的编码方式一样
    rqs.encoding = "gbk"
    return rqs.text


def main():
    index = 1
    details = []
    for times in range(1,4):
        if index == 1:
            html_text = getHtml("http://www.guilin10000.com/scenic/scenic_26.html")
        else:
            html_text = getHtml("http://www.guilin10000.com/scenic/scenic_26_"+str(index)+".html")
        soul = BeautifulSoup(html_text,"html.parser")
        div = soul.find("div",class_ = "s_list")
        li_list = div.find_all("li")
        for li in li_list:
            p_list = li.find_all("p")
            detail = {
                "place" :p_list[0].text,
                "menpiao" : p_list[1].text,
                "jibie" : p_list[2].text,
                "shijian" : p_list[3].text
            }
            details.append(detail)
        index +=1
    for d in details:
        print(d)
    print(len(details))

if __name__ == '__main__':
    main()