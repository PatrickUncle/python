import requests
import time
web = [
    "http://www.yuewct.com",
    "http://www.yuewct.com/book/get_book/bk0059808891/",
    "http://www.yuewct.com/book/get_book/bk0237481337/",
    "http://www.yuewct.com/book/get_book/bk5472623698/",
    "http://www.yuewct.com/book/get_book/bk5487836813/",
    "http://www.yuewct.com/book/get_book/bk9253407173/",
    "http://www.yuewct.com/search/?csrfmiddlewaretoken=Yy76CE7xf5QEMBJTfkyCXs1e00W5ME0P7FwlUKsEBLkpZCcsGd4CJTsJFAatgvsc&kw=%E6%A6%82%E7%8E%87",
    "http://www.yuewct.com/search/?csrfmiddlewaretoken=NknL3u4oaLBDfn9wKBxNkdbcZrvr7ScaWrM0lApvwr5osoC5bu3N6ECHE1JPBJEx&kw=%E6%95%B0%E6%8D%AE%E5%BA%93",
    "http://www.yuewct.com/search/?csrfmiddlewaretoken=OaLZRChw9IIbCChoMHKiT8QFDl5oDZGcXhae9ICDvocWPDKXdAgiFzhaiVjM7Q8z&kw=python",
    "http://www.yuewct.com/user/login/",
    "http://www.yuewct.com/user/register/",
    "http://www.yuewct.com/order/verify/?bk_id=bk5472623698",
    "http://www.yuewct.com/order/verify/?bk_id=bk9253407173",
    "http://www.yuewct.com/book/get_book/bk0059808891/",
    "http://www.yuewct.com/book/get_book/bk0237481337/"
]

while True:
    
    for w in web:
        re = requests.get(w)
        print(re.text)
        time.sleep(2)
    time.sleep(20)
