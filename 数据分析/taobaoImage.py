import requests
import re
import os
import urllib.request
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'COOKIE': 'thw=cn; miid=7654347591112446508; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=%5Cu8D2D%5Cu7269%5Cu53EA%5Cu662F%5Cu4E00%5Cu79CD%5Cu6001%5Cu5EA6; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; enc=TJ0C8nB8X4MTLRnOiLvvrrFhBHR3xRl9w3ILFwCfrLyY5pPZ4smRWMHajZa6LlcT%2BM53U%2BFJwcCktnst0L9BeQ%3D%3D; _uab_collina=154269647131588184803031; t=33555ffd7ae34e798e86900a5f04fe33; Hm_lvt_407473d433e871de861cf818aa1405a1=1553744220,1553752418,1553781240; _cc_=W5iHLLyFfA%3D%3D; cna=ZOSRFaw2TDMCAW87fJKPexek; v=0; cookie2=1d8f47d19a6dc7fb2862797a02e6bcfd; _tb_token_=3e37e9e5ab1b3; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=5eccfbd2c2286199224a8e7189b92054_1563352855830; _m_h5_tk_enc=981647eb44a6c55601aaee94e7f05a65; mt=ci%3D-1_1; x5sec=7b227365617263686170703b32223a22353130303839346663663030383936646432643031373239666666646464363943495351752b6b464549715a3639486468622f5748786f4d4d546b784e4441794d6a51794e6a7378227d; JSESSIONID=9B41828193195EA7CDCFB12C74B0CD21; isg=BAUFcHlk9Kq7wtcTQAQxOoKFFEH_ark__2dKRwdqwTxLniUQzxLJJJN8rILNxdEM; l=cBrkBet4vPCB1tZBBOCanurza77OSIRYYuPzaNbMi_5Q46T1gW_OkD-zXF96VjWdODYB4s6vWjp9-etkqbFn8HQFPiAd'
}
key = '童装'
BASE_PATH = "E:/数据分析/淘宝/淘宝图片"
imagePat = '"pic_url":"//(.*?)"'
namePat = '"raw_title":"(.*?)"'
NUM = 0
for pageIndex in range(2):
    req = requests.get(
        "https://s.taobao.com/list?spm=a21bo.2017.201867-links-0.5.5af911d9WtG4bI&q=" +key+"&cat=16&style=grid&seller_type=taobao&bcoffset=0&s=" + str(pageIndex*60),
        headers=headers)
    req.encoding = 'utf-8'
    imageUrlList = re.compile(imagePat).findall(req.text)
    nameList = re.compile(namePat).findall(req.text)
    print(imageUrlList)
    for index,imageUrl in enumerate(imageUrlList):
        name = nameList[index].replace('/','').replace('\\','')
        fileName = os.path.join(BASE_PATH, name + '.jpg')
        try:
            urllib.request.urlretrieve("http://" + imageUrl, filename=fileName)
            print('-------第' + str(NUM) + '次爬取成功--------')
            NUM += 1
        except:
            print(fileName)
    time.sleep(3)