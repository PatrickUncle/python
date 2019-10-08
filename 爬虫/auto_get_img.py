import requests
from bs4 import BeautifulSoup
import os
import urllib.request as request

type_list = ["xinggan",] #图片类型list

web_dir = {     #类型网页对应字典
    "xinggan":"http://www.mm131.com/xinggan/",
}
Base_path = r"G:\beauty_test"

with open(os.path.join(Base_path,"times.txt"), mode="r", encoding="utf-8") as f:
    times = int(f.readline())

#判断是否有更新,使用txt文件存储最后下载的图片组名字
def is_update(type,re):
    soup = BeautifulSoup(re.text,"lxml")
    imges = soup.find("img",attrs={"width":"120", "height":"160"})
    if type == "xinggan":
        times = 1
    with open("update.txt",mode='r',encoding="utf-8") as  file:
        for i in range(times):
            str = file.readline()
        if str != imges["alt"]:
            return str

#获取即将下载的图组对象，添加入xinggan_list
def get_download_object(re,judge_str):
    download_list = []
    re.encoding="GBK"
    soup = BeautifulSoup(re.text,"lxml")
    list = soup.find_all("img", attrs={"width": "120", "height": "160"})
    for one in list :
        if one["alt"] == judge_str:
            break
        download_list.append(one)
    return download_list

#下载封面与保存名字
def cover_name(img,img_type):
    global times
    times+=1
    file_path = Base_path + "/" + img_type + "/" + str(times)
    while os.path.exists(file_path):
        times+=1
        file_path = Base_path+ "/"+img_type+ "/" + str(times)
    os.makedirs(file_path)
    url = img["src"]
    name = img["alt"]
    with open(file_path+"/"+"name.txt",mode="w",encoding="utf-8") as f :
        f.write(name)
    with open(file_path+"/0.jpg","wb") as f :
        f.write(requests.get(url).content)
    print("保存封面",url,"至：",file_path+"/0.jpg")


#下载详细内容
def details(img,img_type):
    print("进入")
    global times
    details_web = img.parent["href"]
    nums = 2
    url = details_web.replace(".html", "/")
    filepath = Base_path + "/" + img_type + "/" + str(times)
    while True:
        # try:
        print(url +str(nums) + ".jpg")
        request.urlretrieve(url +str(nums) + ".jpg",os.path.join(filepath,str(nums)))
        # except:
        #     break
        print("下载详细内容",img,"至：",os.path.join(filepath,str(nums)))
        nums+=1
def splice_url(url,type,yeshu):
    if type == "xinggan":
        return url + "list_6_%s.html" %yeshu


def main():
    for img_type in type_list:
        yeshu = 1
        url = web_dir[img_type]
        while True:
            if yeshu !=1:
                url = splice_url(url,img_type,yeshu)
            yeshu += 1
            try:
                re = requests.get(url)
                re.encoding="GBK"
            except:
                break
            judge_str = is_update(img_type, re)
            if judge_str:
                download_list = get_download_object(re,judge_str)
                for download in download_list:
                    cover_name(download,img_type)
                    details(download,img_type)

if __name__ == '__main__':
    main()