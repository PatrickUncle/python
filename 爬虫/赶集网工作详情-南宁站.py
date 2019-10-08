import requests
from bs4 import BeautifulSoup
import xlwt
import time
#获取网页的text
def getText(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    return req.text

#处理网页的text文件，获取总的dl_list
def getDL_list(html_text):
    soul = BeautifulSoup(html_text,"html.parser")
    div = soul.find("div",class_ = "f-all-news")
    dl_list = div.find_all("dl")
    return dl_list
#使用dl_list进行遍历，获取所有所有类型
def getWorktype(dl_list):
    typeAndDetals =[]
    index = 0
    # print(dl_list[0])
    for dl in dl_list:
        hrefAndName_list = []
        index+=1
        print(index)
        typeName = dl.find("dt").text
        dd = dl.find("dd")
        a_list = dd.find_all("a")
        if index == 48:
            a_list.pop()
            a_list.pop()
        for a in a_list:
            hrefAndName = {
                "dizhi":a["href"],
                "name":a.string
            }
            hrefAndName_list.append(hrefAndName)
        typeAndDetal ={
            typeName:hrefAndName_list
        }
        typeAndDetals.append(typeAndDetal)
    return typeAndDetals


#得到工作分类后，获取该a标签中href属性，进入详情页面

def getDetalsWeb(href):
    text = getText("http://nn.ganji.com"+ href)
    return text


#进入详情页面后，爬取该详情页面内的work_list
def getWork_list(work_webtext):
    soul = BeautifulSoup(work_webtext,"html.parser")
    dl_list = soul.find_all("dl",class_ = "list-noimg job-list clearfix new-dl")
    return dl_list


#根据work_list来提取所需要的信息
def getUseMasage(work_list):
    work_masage = []
    for work in work_list:
        describe = ""
        i_list = work.find("div",class_="new-dl-tags").find_all("i")
        for i in i_list:
            if i !=None:
                describe +=i.text
        masage = {
        "work_name" : work.find("a",class_ = "list_title gj_tongji").text,
        "company_name" : work.find("div",class_ = "new-dl-company").find("a")["title"],
        "salary" : work.find("div",class_ = "new-dl-salary").text.replace(" ","").replace("\n",""),
        "decsribe" : describe,
        "work_place" : work.find("dd",class_="pay").text
        }
        work_masage.append(masage)

    return work_masage

def main():
    times = 0
    table = "text.xls"
    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("sheet1",cell_overwrite_ok=True)
    headData = ["工作名字","公司名称","薪水","工作地点"]
    current_row = 0
    usemasage_list =[]
    # headers = {
    # "Host": "nn.ganji.com",
    # "Upgrade-Insecure-Requests": "1",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    # }
    print("hhhh")
    html = getText("http://nn.ganji.com/zhaopin/")
    dl_list = getDL_list(html)
    typeAndDetals = getWorktype(dl_list)
    for typeAndDetal in typeAndDetals:
        for type,hrefAndName_List in typeAndDetal.items():
            ws.write(current_row,0,type)
            print("*"*60+type + "*"*60)
            current_row =current_row +1
            print("当前行："+str(current_row))
            for hrefandname in hrefAndName_List:
                href = hrefandname["dizhi"]
                text = getDetalsWeb(href)
                work_list = getWork_list(text)
                usemasage = getUseMasage(work_list)
                time.sleep(2)
                for user in usemasage:
                    ws.write(current_row,0,user["work_name"])
                    print(user["work_name"])
                    print(user["company_name"])
                    print(user["salary"])
                    print(user["decsribe"])
                    print(user["work_place"])
                    ws.write(current_row,1,user["company_name"])
                    ws.write(current_row,2,user["salary"])
                    ws.write(current_row,3,user["decsribe"])
                    ws.write(current_row,4,user["work_place"])
                    times+=1
                    print("-"*50+str(times)+"-"*50)
                    current_row = current_row+1
                    print("当前行："+str(current_row))
    wb.save(r"C:\Users\ASUSPC\Desktop\test.xlsx")

if __name__ == '__main__':
    main()