import requests
from bs4 import  BeautifulSoup
import json

# response = requests.get("http://localhost:63343/%E5%93%81%E5%B1%85/index.html?_ijt=u6ts3dldm83mvrc02e2s5ob7ar")
# print(response.content)


def main():
    head ={
    "Host": "tianqi.so.com",
    "Referer": "https://tianqi.so.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"

}
    result = requests.get("https://tianqi.so.com/weather/101300501",headers = head)
    # print(result.content.decode("utf-8"))
    html_text = result.text
    bs = BeautifulSoup(html_text,"html.parser")
    body = bs.body
    data = body.find("div",{"class":"weather-card"})
    ullist = data.find_all("ul")
    # print(ullist)

    for ul in ullist:
        divlist = ul.find_all("div")
        riqi = divlist[1].text
        qingkuang = divlist[3].text.replace(" ","")
        qingkuang = qingkuang.replace("\n","")
        temperature = divlist[4].text
        isgood = divlist[5].text
        wind = divlist[6].text
        # print(divlist)
        print(riqi)
        print(qingkuang)
        print(temperature)
        print(isgood)
        print(wind)
        
        print("\n")


if __name__ == '__main__':
    main()