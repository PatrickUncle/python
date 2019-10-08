import requests
from bs4 import BeautifulSoup

group_url_dir ={

}
#大页面的头部信息
web_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
    "Connection": "keep-alive",
    "Cookie": "UM_distinctid=16508c3008024d-0eba529d32b883-47e1f32-144000-16508c30083551; CNZZDATA3866066=cnzz_eid%3D1525886784-1494676185-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1494676185; bdshare_firstime=1533450322231; Hm_lvt_9a737a8572f89206db6e9c301695b55a=1533450322,1533450417,1533450737,1533654047; Hm_lpvt_9a737a8572f89206db6e9c301695b55a=1533657834",
    "Referer": "http://www.mm131.com/xinggan/",
}

#生成网页的url
def create_web_url(first_url,belong,yeshu):
    url_list = []
    url_list.append(first_url)
    if belong == "xinggan":
        for i in range(2,yeshu+1):
            url_list.append(first_url+"list_6_%s.html"%(i))
    elif belong == "qingchun":
        for i in range(2, yeshu + 1):
            url_list.append(first_url + "list_1_%s.html" % (i))
    elif belong == "chemo":
        for i in range(2, yeshu + 1):
            url_list.append(first_url + "list_3_%s.html" % (i))
    elif belong == "xiaohua":
        for i in range(2, yeshu + 1):
            url_list.append(first_url + "list_2_%s.html" % (i))
    elif belong == "qipao":
        for i in range(2, yeshu + 1):
            url_list.append(first_url + "list_4_%s.html" % (i))
    elif belong == "mingxing":
        for i in range(2, yeshu + 1):
            url_list.append(first_url + "list_5_%s.html" % (i))
    return url_list

#获取每组图片的下载链接
def get_img_group_url(belong,web_list):
    group_url_dir[belong]=[]
    for web in web_list:
        re = requests.get(web,headers = web_headers)
        re.encoding="gb2312"
        soup = BeautifulSoup(re.text,"lxml")
        dl = soup.find("dl",attrs={'class':"list-left public-box",})
        a_list = dl.find_all("a",attrs={'target':"_blank"})
        for a in a_list:
            img = a.find("img")
            one_group = {
                "name":a.text,
                "href":a["href"],
                "cover":img["src"],
            }
            group_url_dir[belong].append(one_group)
#获取该组全部图片url
def get_img_url(img_href):
    pass
#下载图片，并且确定使用的存放地址
def download_img():
    pass
def get_dir():
    xinggan_first_web_url = "http://www.mm131.com/xinggan/"
    xinggan_web_list = create_web_url(xinggan_first_web_url,"xinggan",153)
    get_img_group_url("xinggan",xinggan_web_list)

    qingchun_first_web_url = "http://www.mm131.com/qingchun/"
    qingchun_web_list = create_web_url(qingchun_first_web_url,"qingchun",31)
    get_img_group_url("qingchun",qingchun_web_list)

    xiaohua_first_web_url = "http://www.mm131.com/xiaohua/"
    xiaohua_web_list = create_web_url(xiaohua_first_web_url,"xiaohua",6)
    get_img_group_url("xiaohua",xiaohua_web_list)

    chemo_first_web_url = "http://www.mm131.com/chemo/"
    chemo_web_list = create_web_url(chemo_first_web_url,"chemo",10)
    get_img_group_url("chemo",chemo_web_list)

    qipao_first_web_url = "http://www.mm131.com/qipao/"
    qipao_web_url = create_web_url(qipao_first_web_url,"qipao",4)
    get_img_group_url("qipao",qipao_web_url)

    mingxing_first_web_url = "http://www.mm131.com/mingxing/"
    mingxing_web_list = create_web_url(mingxing_first_web_url,"mingxing",8)
    get_img_group_url("mingxing",mingxing_web_list)

def main():
    # get_dir()
    pass
if __name__ == '__main__':
    main()