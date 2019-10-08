import requests
from bs4 import BeautifulSoup

re = requests.get("https://www.guet.edu.cn/info/1151/48410.htm")
re.encoding = "utf-8"
soup = BeautifulSoup(re.text,"html.parser")
div = soup.find("div",id="newsContent")
p_list = div.find_all("p")
for p in p_list:
    if p.text == "":
        break
    else:
        print(p.text)