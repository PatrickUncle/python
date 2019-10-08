import requests         #请求
import urllib.request   #下载图片
from bs4 import BeautifulSoup
import os
import time

class beauty(object):

    def __init__(self,belong,web_url,first_group_title):
        print("正在初始化"+"."*6)
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),"   当前类型：",belong)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "   当前访问页面：", web_url)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "   以往第一组图片名：", first_group_title)
        self.belong = belong
        self.web_url = web_url
        self.first_title = first_group_title

    def is_update(self):
        self.soup = self.get_soup(self.web_url)
        div = self.soup.find("div",attrs={"class":"name"})
        if div.find("a")["title"] == self.first_title:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"类型“"+self.belong+"”已经是最新的了，不需要更新！")
            return False
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "类型“" + self.belong + "”有新的图组更新，开始更新！")
        return True

    def get_download_group(self):
        download_list = []
        div_list = self.soup.find_all('div',attrs={"picbox"})
        for div in div_list:
            img = div.find("img")
            one_data = {
                "group_title" : img["alt"],
                "group_url" : "https://www.zbjuran.com" + div.find("a")["href"],
            }
            if "http://" in img["data-original"]:
                one_data["group_cover"] = img["data-original"]
            else:
                one_data["group_cover"] = "https://www.zbjuran.com" + img["data-original"]
            if one_data["group_title"] == self.first_title:
                break
            download_list.append(one_data)
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "类型“" + self.belong + "”需要更新",str(len(download_list)),"组图片！")
        return download_list

    def download(self,download_group):
        global beauty_id
        beauty_id += 1
        for group_dict in download_group:
            title = group_dict["group_title"]
            cover = group_dict["group_cover"]
            group_url = group_dict["group_url"]
            file_path = Base_path + "/" + self.belong + "/" + str(beauty_id)
            while os.path.exists(file_path):
                beauty_id += 1
                file_path = Base_path + "/" + self.belong + "/" + str(beauty_id)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "当前使用的id为：", beauty_id)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "保存路劲为：", file_path)
            os.makedirs(file_path)
            with open(os.path.join(file_path,"name.txt"),mode="w",encoding="utf-8") as f:
                f.write(title)
            self.auto_down(cover,os.path.join(file_path,"0.jpg"))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "下载封面：", cover,"完毕.........")
            soup = self.get_soup(group_url)
            img_url = "https://www.zbjuran.com" + soup.find("div",attrs={"class":"picbox"}).find("img")["src"]
            self.auto_down(img_url,os.path.join(file_path,"1.jpg"))
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "下载图片：", img_url, "完毕.........")
            #获取图片数量
            for page in range(2,int(soup.find("div",attrs={"class":"page"}).find("a").text.split("页")[0].split("共")[1]) + 1):
                soup = self.get_soup(group_url.replace(".html","") + "_%s"%page + ".html")
                img_url = "https://www.zbjuran.com" + soup.find("div", attrs={"class": "picbox"}).find("img")["src"]
                # urllib.request.urlretrieve(img_url, os.path.join(file_path, "%s.jpg"%page))
                self.auto_down(img_url,os.path.join(file_path, str("%s.jpg"%page)))
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "下载图片：", img_url, "完毕.........")
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "下载",title+"图组完成.......")


    def get_soup(self,url):
        re = requests.get(url)
        re.encoding="GBK"
        soup = BeautifulSoup(re.text, "lxml")
        return soup

    def auto_down(self,url,filename):        #解决出现下载文件太小，进行递归下载
        try:
            urllib.request.urlretrieve(url,filename)
        except:
            self.auto_down(url.filename)


Base_path = r"G:\beauty_test"

beauty_id = 0
with open("beauty_id.txt",mode="r",encoding="utf-8") as file:
    beauty_id = int(file.readline())

def main():
    #类型字典
    type_dict = {
        "xinggan":"https://www.zbjuran.com/mei/xinggan/",
        "qingchun":"https://www.zbjuran.com/mei/qingchun/",
        "mingxing":"https://www.zbjuran.com/mei/mingxing/",
        "xiaohua":"https://www.zbjuran.com/mei/xiaohua/",
    }
    type_list = []    #类型列表
    beauty_txt = []

    with open("beauty.txt",mode="r",encoding="utf-8") as file:
        for line in file.readlines():
            type_list.append(line)   #strip 去掉末尾的"\n"
    print("-" * 30 + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "-" * 30)
    for i,(belong,web_url) in enumerate(type_dict.items()):    #enumerate可以让列表产生一个序号
        #生成相对应对象
        work = beauty(belong=belong, web_url=web_url,first_group_title=type_list[i].strip())
        #判断是否有需要更新下载的组
        if work.is_update() :
            #如果有需要更新的组，则获取需要下载的组列表
            download_group = work.get_download_group()
            # #利用需要下载的列表下载对应封面及其详细内容

            work.download(download_group)
            beauty_txt.append(download_group[0]["group_title"] + "\n")
        else:
            beauty_txt.append(" ")
    with open("beauty_id.txt",mode="w",encoding="utf-8") as f :
        f.write(str(beauty_id))
    with open("beauty.txt",mode="w",encoding="utf-8") as f :
        neirong = ""
        for i , content in enumerate(beauty_txt):
            if content == " ":
                print("添加前:",neirong)
                neirong += type_list[i]
                print("添加后:",neirong)
            else:
                print("添加前:", neirong)
                neirong += content
                print("添加后:", neirong)
        f.write(neirong)

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),"结束扫描")
    print("-" * 30 + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "-" * 30)

if __name__ == '__main__':
    main()