import requests

from bs4 import BeautifulSoup
def get_more_school(url_web):
    school_name = []
    re = requests.get(url_web)
    re.encoding = "GBK"
    soup = BeautifulSoup(re.text,"lxml")
    table_list = soup.find_all("td",attrs={"class":"tdbg_title"})
    table_list.remove(table_list[0])
    for table in table_list:
        name = table.find("h4").text
        school_name.append(name)
    return school_name
def get_details_url(table):
    url = table.find("a",attrs={"class":"daxueright"})["href"]
    return url
# get_more_school("https://www.unjs.com/daxue/guangxi/")
result_dict = {}
province_list = []
re = requests.get("https://www.unjs.com/")
re.encoding = "GBK"
soup = BeautifulSoup(re.text,'lxml')
table = soup.find("table",class_="tdbg_none")
table_list = table.find_all("table")
table_liebiao = []
for i,gaoxiao in enumerate(table_list):
    if i % 2 == 1:
        continue
    table_liebiao.append(gaoxiao)
for i,gaoxiao in enumerate(table_liebiao):

    gaoxiaomingzi = gaoxiao.find("strong")
    name = gaoxiaomingzi.text.replace("高校","")
    province_list.append(name)
    url_web = get_details_url(gaoxiao)
    school_list = get_more_school(url_web)
    result_dict[province_list[i]] = school_list
print(result_dict)
# print(table_list)