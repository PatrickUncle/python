import requests
import time
from bs4 import BeautifulSoup

file = open("dubodata.txt",mode='a',encoding='utf-8')
yeshu = 1981
data = {
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0,
    '10':0,
}
headers={
    'Cookie' : 'ASP.NET_SessionId=cjm0elykpfbhjeq5jsle5yqf',
    'Host': '103.20.193.42',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'http://103.20.193.42/Pk10/List.Aspx?Cid=null&v=1&page=1',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
}

def create_url():
    url_list =[]
    url = "http://103.20.193.42/pk10/List.Aspx?&Cid=null&v=1"
    url_list.append(url)
    url +="&page="
    for i in range(2,1981):
        url = "http://103.20.193.42/pk10/List.Aspx?&Cid=null&v=1&page=" + str(i)
        url_list.append(url)
    return url_list


def get_data(url):
    try:
        request = requests.get(url,headers=headers)
    except:
        time.sleep(5)
        request = requests.get(url, headers=headers)
    time.sleep(2)
    if request.status_code == 200:
        request.encoding = 'utf-8'
    #     # print(request.text.replace("<br>","").replace("<br/>",""))
        soup = BeautifulSoup(request.text.replace("<br>","").replace("<br/>",""),"lxml")
        body = soup.find(name="body").text
        data = body.split("】")[1].split("[")[0]
        num = data.split("期")[0]
        num = int(num)
        for i in range(15):
            now_num = num-i
            tihuan = str(now_num)+"期"
            data = data.replace(tihuan," ")
        data_list = data.split(" ")[14::-1]
        i = 15
        for one_data in data_list:
            i-=1
            if i !=0:
                file.write(one_data + "\n" )
            else:
                file.write(one_data)
        file.flush()
def main():
    global yeshu
    url_list = create_url()
    for url in url_list[1980::-1]:
        get_data(url)
        print("第",yeshu,"页数据写入完毕！！！！！！！！！！！",)
        yeshu-=1

if __name__ == '__main__':
    main()