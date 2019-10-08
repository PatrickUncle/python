# print("-------------我爱潘淑虹--------------")
# temp = input("输入：")
# guess = int(temp)
# if guess == 8:
#     print("you are right")
# else:
#     print("error")
#     print("game over")

# num = 32
# print("我的名字是："+str(num))

# num = [1,2,3,4,5,6,7,8,9]
# print(num[1::])

# p = ["a","v","g","w"]
# result = ""
# for o in p:
#     result += o
# print(result)
# import django
# print(django.__version__)

# h = 100000000000000000000000000000009999999559
# l = 888888888876654564564654654
# print(h*l)
# import threading
# ss = threading.Lock
# import _thread
# _thread.
# import threading
# #
#
# value_lock = threading.Lock()
# value_lock.acquire()
# value_lock.release()

# sss = [(0,1),(1,0),(-1,0),(0,-1)]
# sss.remove((1,0))
# for k in sss:
#     print(k)
# try:
#     liebiao = [0,1,8,3,4,5]
#     s = liebiao.index(2)
#     print(s)
# except ValueError:
#     print("aaa")
# ll = (1,2)
# print(ll)

# ll = [1,0]
# pp = [-ll[0],-ll[1]]
# print(pp)

# ll = [
#     [1,2,3,5],
#     [0,8,9,7]
# ]
# print(ll[0][0])
# class SharedCounter:
#     '''
#       一个可以由多个线程共享的计数器对象
#     '''
#     def __init__(self, initial_value = 0):
#         self._value = initial_value #计数器值初始化
#         self._value_lock = threading.Lock() #实例化
#
#     def incr(self,delta=1):
#         '''
#         通过锁递增计数器
#         '''
#         self._value_lock.acquire()
#         self._value += delta
#         self._value_lock.release()

# import math
# math.tan()
#
#     def decr(self,delta=1):
#         '''
#         通过锁递减计数器
#         '''
#         self._value_lock.acquire()
#         self._value -= delta
#         self._value_lock.release()

# def mmm():
#     for x in range(0,100):
#         print(x)
# for x in range(4):
#     threading.thread
# class lei:
#     liebiao = [0]
#
# p = lei()
# print(id(p.liebiao))
# p.liebiao = p.liebiao[0] + 1
# p.liebiao = []
# print(id(p.liebiao))
# b = lei()
# p.liebiao.append(b)
# print(p.liebiao)

# class lei():
#     a = 0
#     print("1")

# p = 1
# h = "5"
# print(h)
# print(type(h))
# print(p)
# print(type(p))
#
# print(str(p) + h)

# class lei:
#     p = 0
#
# p = lei()
# q=p
# print(p)
#
# p.p= 1
# print(p)
# print(q.p)
# x = 2
# y = 6
# if 1 < x < 2:
#     print("aa")
#
# zidian ={
#     "hanyu":"汉语字典",
#     "yingyu":"英语字典"
# }
#
# print(zidian["hanyu"])
# print(zidian["yingyu"])

# k = [0,1]
# p = [1,0]
#
# if k == p:
#     print("yes")
# k = [1,0]
# k.remove("None")

# kk = {
#     "ssss":{
#         "ssss":"aaaa",
#         "wwwww":"llll"
#     },
#     "sqaw":{
#         "ssshhs":"aaaa",
#         "wwwhhw":"llll"
#     }
# }
# from tkinter import *
# root = Tk()
# root.title('试试文本框右键菜单')
# root.resizable(False, False)
# root.geometry("300x100+200+20")
# Label(root, text='下面是一个刚刚被生成的文本框，试试操作吧').pack(side="top")
# Label(root).pack(side="top")
# show = StringVar()
# Entry = Entry(root, textvariable=show, width="30")
# Entry.pack()
# class section:
#     def onPaste(self):
#         try:
#             self.text = root.clipboard_get()
#         except TclError:
#             pass
#         show.set(str(self.text))
#     def onCopy(self):
#         self.text = Entry.get()
#         root.clipboard_append(self.text)
#     def onCut(self):
#         self.onCopy()
#         try:
#             Entry.delete('sel.first', 'sel.last')
#         except TclError:
#             pass
# section = section()
# menu = Menu(root, tearoff=0)
# menu.add_command(label="复制", command=section.onCopy)
# menu.add_separator()
# menu.add_command(label="粘贴", command=section.onPaste)
# menu.add_separator()
# menu.add_command(label="剪切", command=section.onCut)
# def popupmenu(event):
#     menu.post(event.x_root, event.y_root)
# Entry.bind("<Button-3>", popupmenu)
# root.mainloop()

# import requests
# from bs4 import BeautifulSoup
#
# req = requests.get("http://study.163.com/courses")
# req.encoding="utf-8"
# soup = BeautifulSoup(req.text,"html.parser")
# print(soup)
# print(kk["ssss"])


# ll = [
#     {"aaa":1,
#     "www":2
#     }
#     ,
#     {
#         "wwww":2222,
#         "wwwgg":5884
#     }
# ]
#
# print(ll[0]["aaa"])
# import time
#
# for i in range(0,100):
#     time.sleep(1)
#     print(i)
# q  =[]
# p = []
# nnn = {
#     "aa":13
# }
# p.append(nnn)
# detal = {
#     "mm":nnn
# }
# q.append(detal)
# print(q)
# nnn ={
#     "qq":55
# }
# detal = {
#     "qq":nnn
# }
# q.append(detal)
# print(q)
# import django
# print(django.get_version())

# a ={}
# a.update(p = 1)
# print(a)
#
# print('p' in a)
# data ={'1':0}
# # data["1"] +1
# # print(data)
# print(data['1'])
# data = {
#     '1':0
# }
# i = 1
# print(data[str(i)])
# p = [5,6,7]
# print(p.index(6))

# class A(object):
#     def p(self):
#         print("wuwu")
#     def k(self):
#         pass
#
#
# class B(A):
#     def p(self):
#         print("haha")
#
#
# a = A()
# a.p()
#
# b = B()
# b.p()

# a = "aaa"
# p={}
# p[a]=1
# print(p)
# if False:
#     print("a")
# import time
# print(time.time())
# print(time.localtime())
# print(time.localtime(time.time()))
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# import os
#
# # base = os.path.abspath(__file__)
# # print(os.path.join(base,"haha"))
# #
# # print(os.path.abspath(__file__))
#
# # def num(i):
# #     i+=1
# #     print(i)
# # p = 5
# # num(p)
# # print(p)
# # i = True
# # if not i:
# #     print("hhh")
#
# # url = "http://www.mm131.com/xinggan/4262.html"
# # url = url.replace(".html","")
# # print(url)
# # import urllib.request as request
# # url = "http://img1.mm131.me/pic/4264/1.jpg"
# #
# # request.urlretrieve(url,"1.jpg")
# #
# # with open("1.jpg","wb") as f :
# #     f.write((request.urlopen(url)).read())
#
# # import requests
# #
# # headers = {
# #     "Referer": "http://www.mm131.com/xinggan/4265_3.html",
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
# # }
# # with open("1.jpg","wb") as f :
# #     f.write(requests.get("http://img1.mm131.me/pic/4265/3.jpg",headers=headers).content)
# # import base64
# # a= base64.b64decode("jd8tw2l8hcvaj1jh01imzi9hiexpulvo")
# # a = str(a)
# # a.encode("utf-8")
# # print(a)
# # print("h")
# # import urllib.request
# #
# # urllib.request.urlretrieve("http://www.zbjuran.com/uploads/imgs/07/eqy0fx0doet.jpg","1.jpg")
# # https://www.zbjuran.com/mei/
# # a = [1,2,3]
# # a.pop()
# # print(a)
# # print(a.next())
# # a = "共5页: "
# # print(a.split("页")[0].split("共")[1])
# # a = 1
# # print("o_%s"%a)
# # import urllib.request
# # print(urllib.request.__version__)
# # a ="a"
# # b = "b"
# # a += b
# # print(a)
# # import os
# # Base_path = r"G:\beauty_test"
# # type_list = os.listdir(Base_path)
# # for type_name in type_list:
# #     type_path = os.path.join(Base_path, type_name)
# #     id_list = os.listdir(type_path)
# #     for xuhao in id_list:
# #         name_path = os.path.join(os.path.join(type_path,xuhao),'name.txt')
# #         print(name_path)
# # a = {"a":1,"b":2}
# # print(list(a.keys()))
# # a=[1,2,3,4,5]
# #
# # print(a[-1:-3:-1])
# # a = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '4', '40', '41', '42', '43', '44', '45', '5', '6', '7', '8', '9']
# # a.sort()
# # int_list = []
# # str_list= []
# # for i in a :
# #     int_list.append(int(i))
# # int_list.sort()
# # for i in int_list:
# #     str_list.append(str(i))
# # print(str_list)
# # p = "http://www.zbjuran.com/uploads/allimg/170814/2-1FQ4140A2352.jp"
# # if "http://" in p:
# #     print("hehe")
# # def hello(**args):
# #     print(args)
# #
# #
# # hello(name=1,p=2)
# # data = {
# #     "success":True,
# #     "dada":"asda",
# # }
# # print(data)
# # print(type(data["success"]))
# # print(data["success"])
# # if data["success"]:
# #     print("hh")
#
# # def ceshi():
# #     print("hello")
#
# # i = 31
# # print(len(i))
# # i = 10
# # print(str(i))
# # print(len("10"))
# # print("0"*(3-len(str(i))) + str(i))
# # print(2/5)
# # p = [1,2,3]
# # p.reverse()
# # print(p)
# # dd = {
# #     "a":1,
# #     "b":2
# # }
# # print("c" in dd.keys())
# # import matplotlib
# # print(matplotlib.matplotlib_fname())
# # l = ["a","b","c"]
# # if "q" not in l:
#     # print("hello")
# # print(l[0:2:1])
# # import requests
# # re = requests.get('https://api.douban.com/v2/book/isbn/9787302099666')
# # print(re.text)
# import ssl, hmac, base64, hashlib
# from datetime import datetime as pydatetime
#
# try:
#     from urllib import urlencode
#     from urllib2 import Request, urlopen
# except ImportError:
#     from urllib.parse import urlencode
#     from urllib.request import Request, urlopen
#
# # 云市场分配的密钥Id
# secretId = "AKIDAxmnk3ie5b60PF8VoWF79fJYSJffNr0ThuwM"
# # 云市场分配的密钥Key
# secretKey = "aU62AhSF0x67ne1KcA464TO1rSBg49bkYzKS4JP0"
# source = "market"
#
# # 签名
# datetime = pydatetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
# signStr = "x-date: %s\nx-source: %s" % (datetime, source)
# sign = base64.b64encode(hmac.new(secretKey.encode('utf-8'), signStr.encode('utf-8'), hashlib.sha1).digest())
# auth = 'hmac id="%s", algorithm="hmac-sha1", headers="x-date x-source", signature="%s"' % (secretId, sign.decode('utf-8'))
#
# # 请求方法
# method = 'GET'
# # 请求头
# headers = {
#     'X-Source': source,
#     'X-Date': datetime,
#     'Authorization': auth,
# }
# # 查询参数
# queryParams = {
#     'isbn': '9787302390626'}
# # body参数（POST方法下存在）
# bodyParams = {
# }
# url参数拼接
# url = 'https://service-osj3eufj-1255468759.ap-shanghai.apigateway.myqcloud.com/release/isbn'
# if len(queryParams.keys()) > 0:
#     url = url + '?' + urlencode(queryParams)
#
# request = Request(url, headers=headers)
# request.get_method = lambda: method
# if method in ('POST', 'PUT', 'PATCH'):
#     request.data = urlencode(bodyParams).encode('utf-8')
#     request.add_header('Content-Type', 'application/x-www-form-urlencoded')
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# response = urlopen(request, context=ctx)
# content = response.read()
# if content:
#     print(content.decode('utf-8'))
#
# f = open("E:/数据分析/1.txt",'w')
# f.write("asdasd")
import re
s = '<div class="sku-name">       \n联想ThinkPad 翼480（4VCD）英特尔酷睿i5 14英寸轻薄窄边框笔记本电脑（i5-8250U 8G 128GSSD+1T 2G独显 FHD高清显示屏）冰原银           </div>'
result = re.search(r'<div class="sku-name">(.*?)</div>',s.replace("\n","")).group(1)
print(result)