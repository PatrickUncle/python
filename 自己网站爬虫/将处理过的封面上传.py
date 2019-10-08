import requests
import os
import time

web_url = "http://www.yuewct.com:8000/reload/"
BASE_PATH = r"F:\处理过的封面"

data = {
        "csrfmiddlewaretoken": "",
        "book_id":""
    }

def GetSession():
    s = requests.session()
    re = s.get(web_url)
    data["csrfmiddlewaretoken"] = re.cookies["csrftoken"]
    return s

def CoverList():
    return os.listdir(BASE_PATH)

def Send(filename,s):
    data["book_id"] = filename.split("_")[0]
    print(data)
    f = open(os.path.join(BASE_PATH,filename),"rb")
    r = s.post(web_url,data=data,files={"file":f})
    f.close()
if __name__ == '__main__':
    s = GetSession()
    cover_list = CoverList()
    for cover in cover_list:
        Send(cover,s)
        time.sleep(1)