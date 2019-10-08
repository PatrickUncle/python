import requests
import re
import os

req = requests.get('https://www.sina.com.cn/')

pat = '<a target="_blank" href="(http\w.*?)">.*?</a>'

data = req.text

hrefList = re.compile(pat).findall(data)

print(hrefList)
for url in hrefList:
    try:
        req = requests.get(url)
        req.encoding = 'utf-8'
        data = req.text
        titlePat = '<h1 class="main-title">(.*?)</h1>'
        contentPat = '<p>([^All Rights Reserved|Copyright].*?)</p>'
        title = re.search(pattern=titlePat,string=data)
        if title :
            title = str(title.group(1))   #group（） 返回匹配到的内容 不加参数代表返回整个pat匹配的数据，加了参数1 代表返回括号里面的内容
            contentList= re.compile(pattern=contentPat).findall(data)
            fileName = "E:/数据分析/" + title + ".txt"
            print(fileName)

            f = open(fileName, 'w')
            for content in contentList[1::]:
                f.write(content + "\n")
            f.close()
    except:
        pass

