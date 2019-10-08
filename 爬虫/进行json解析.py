import json
import requests
headers = {
    "referer": "https://item.jd.com/5225346.html",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
}

response = requests.get("https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv22524&productId=5225346&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1",headers=headers)
# print(response.text)
response.encoding = "GBK"
print(response.text)
# json_str = response.text
# unicodestr = json.loads(json_str)
# print(unicodestr)
