import requests
import re
import json
import xlrd
from xlutils.copy import copy
import time

pcType = "SAMSUNG"

namePat = r'<div class="sku-name">(.*?)</div>'
skuIdPat = r'https://item.jd.com/(.*?).html'
catPat = r"cat=(.*?)&ev=exbrand"
count = 0
headers = {
    "COOKIE":"shshshfpa=8c3c41d7-9763-0391-298a-15da81cc7568-1536329346; shshshfpb=05b2d337c1314b666471fa9cb627d4fb6892dc341c26e9c4c5b9286831; __jdu=15232673291491792532832; pin=%E6%97%A7%E4%B9%A6%E6%90%AC%E8%BF%90%E5%B7%A5; unick=%E6%97%A7%E4%B9%A6%E6%90%AC%E8%BF%90%E5%B7%A5; _tp=PCmUSywGtjdJMufeUDWgcUCn6%2BSa%2F%2FTgmtKhwhWrg5g1FHTb6RRHJp6xBTgLFg%2F7; _pst=%E6%97%A7%E4%B9%A6%E6%90%AC%E8%BF%90%E5%B7%A5; user-key=89bc8b9a-b772-42d5-b333-b50157aedbd7; areaId=20; ipLoc-djd=20-1818-1822-12483.1429879035; ipLocation=%u5e7f%u897f; cn=0; PCSYCityID=CN_440000_440100_440106; unpl=V2_ZzNtbRYEQEZ1D09cfxhbDWIHQF9KB0QUJVtFBHxJXwE0A0IJclRCFX0UR11nGlsUZAEZXkJcQxJFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsdXwdkBBRfQV9DEH0IQFx4HV4GbgERbXJQcyVFDURSfxhdNWYzE20AAx8WdQBDUXNUXAFkARFaRFVAHXUNTlR9EV8BZQAbX0FnQiV2; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_eb2b1689506945c39a60ab2a6a25b1ae|1566832942252; shshshfp=585748c7b5a4a6a2f92f87e7cf32dc86; 3AB9D23F7A4B3C9B=7MONFITY2AP6O7WML2KA2D523HP4QZ35FOCV7ZOVJVFW7K7IFQPH6ZOZL5STNF5TW43SRUSWAQENL5XDKTRM6ZG5M4; __jda=122270672.15232673291491792532832.1523267329.1566832555.1566870614.19; __jdc=122270672; shshshsID=92ae769478169f34a2e8ecf0181ee3c3_4_1566871097383; __jdb=122270672.4.15232673291491792532832|19.1566870614",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
# 获取名字
def getName(req):
    return re.search(namePat,req.text.replace("\n","")).group(1).replace(" ",'')

# 获取评价内容
def getTalk(req):

    talkContent = json.loads(req.text)
    talkDict = {
        "zongping":talkContent["CommentsCount"][0]["CommentCount"],
        "pingjunfen":talkContent["CommentsCount"][0]["AverageScore"],
        "haoping":talkContent["CommentsCount"][0]["GoodCount"],
        "zhongping":talkContent["CommentsCount"][0]["GeneralCount"],
        "chaping":talkContent["CommentsCount"][0]["PoorCount"]
    }
    return talkDict

# 获取价格内容
def getPrice(req):
    priceContent = json.loads(req.text)

    return priceContent["stock"]["jdPrice"]["p"]

def save(name,price,talkDict,url):
    xlFile = xlrd.open_workbook(r"F:/1python/scrapy爬虫/pc/各大电脑品牌内容/电脑数据.xls")
    row = xlFile.sheets()[0].nrows
    excel = copy(xlFile)
    table = excel.get_sheet(0)
    print("已经拥有"+str(row)+"条数据")
    table.write(row,0,pcType)
    table.write(row,1,name)
    table.write(row,2,price)
    table.write(row,3,talkDict["zongping"])
    table.write(row,4,talkDict["haoping"])
    table.write(row,5,talkDict["zhongping"])
    table.write(row,6,talkDict["chaping"])
    table.write(row,7,talkDict["pingjunfen"])
    table.write(row,8,url)
    excel.save(r"F:/1python/scrapy爬虫/pc/各大电脑品牌内容/电脑数据.xls")
def main():
    global count
    with open(r"F:/1python/scrapy爬虫/pc/各大电脑品牌内容/三星.txt", "r") as f:
        line = f.readline()

        while line:
            try:
                pcUrl = "https://" + line.split("//")[1]
                print(pcUrl)
                req = requests.get(pcUrl,headers=headers)
                # 获取名字
                name = getName(req)
                print(name)
                webText = req.text
                # p-name 名字

                # 价格
                skuId = re.search(skuIdPat,pcUrl).group(1)
                print(skuId)
                cat = re.search(catPat,webText).group(1).split("&tid")[0]
                print(cat)
                priceUrl = 'https://c0.3.cn/stock?area=20_1818_1822_12483&buyNum=1&extraParam={"originid":"1"}&pdpin=旧书搬运工&skuId='+skuId+'&cat='+cat
                priceReq = requests.get(priceUrl,headers=headers)
                # time.sleep(0.5)
                price = getPrice(priceReq)
                print(price)


                talkUrl = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds=' + skuId
                talkReq = requests.get(talkUrl,headers=headers)
                talkDict = getTalk(talkReq)
                print(talkDict)
                # count += 1
                # print("asdasssssssss",count)
                save(name,price,talkDict,pcUrl)

            except:
                pass
            line = f.readline()
if __name__ == '__main__':
    main()