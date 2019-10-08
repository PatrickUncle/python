from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
import time
import tkinter as tk
import threading
from PIL import Image


class login(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://web2.qq.com/")
        self.driver.switch_to_frame("ptlogin")
        self.img = self.driver.find_element_by_class_name("qrImg")
        self.img_url = self.img.get_attribute("src")
        self.driver.save_screenshot(r"interface.png")
        # 882 411
        x = self.img.location["x"] + 177
        y = self.img.location["y"] + 83
        endX = x + self.img.size["width"] + 30
        endY = y + self.img.size["height"]+ 30
        picture  = Image.open(r"interface.png")
        erweima = picture.crop((x,y,endX,endY))
        erweima.save(r"erweima.png")

    def is_saomiao_success(self):
        #退出特定的iframe
        self.driver.switch_to_default_content()
        while True:
            try:
                self.driver.find_element_by_class_name('login-title')
            except:
                return True
            time.sleep(0.5)

    def get_group(self):
        self.driver.implicitly_wait(5)
        lianxiren = self.driver.find_element_by_class_name('conversation')
        lianxiren.click()
        self.driver.implicitly_wait(2)
        #组名与div的对应 如：{'我的好友' : 对应该div}
        self.group_dir = {}
        group_list = []
        self.div_group_list = self.driver.find_elements_by_class_name('list_group')
        for group in self.div_group_list:

            div= group.find_element_by_tag_name('div')
            span = div.find_element_by_tag_name('span')
            #处理元素 is_displayed() 返回false 方法
            group_name = span.get_attribute('textContent')
            group_list.append(group_name)
            self.group_dir[group_name] = group
        return group_list
    def get_person_list(self,group):
        div = self.group_dir[group]
        div.click()
        # 获取该组下的所有人
        person_list = div.find_elements_by_class_name('list_item')
        return  person_list
    def send_masage(self, person, masage):
        try:
            person.click()
            time.sleep(1)
            textarea = self.driver.find_element_by_id("chat_textarea")
            textarea.send_keys(masage)
            time.sleep(0.5)
            bt = self.driver.find_element_by_id('send_chat_btn')
            bt.click()
            return person.find_element_by_class_name("member_nick").text
        except:
            return False


    def stop(self):
        self.driver.quit()
check_list = []
user = login()
windows = tk.Tk()
var_list=[]
group_list = []

def saomiao():
    while True:
        if user.is_saomiao_success():
            tk.Label(windows, text="请稍后.........").pack()
            global group_list
            group_list = user.get_group()
            tk.Label(windows, text="②请选择你需要发送消息的分组").pack()
            for group in group_list:
                var = tk.IntVar()
                check = tk.Checkbutton(windows, text=group,variable=var)
                var_list.append(var)
                check_list.append(check)
                check.pack()
            tk.Label(windows,text="③请输入你要群发送的信息内容！").pack()

            entry = tk.Entry(windows)
            entry.pack()

            bt = tk.Button(windows, text="开  始", command=lambda : action(entry))
            bt.pack()
            break
def action(entry):
    selected_list= []
    for i,var in enumerate(var_list,0):
        if var.get() == 1:
            selected_list.append(group_list[i])
    text = tk.Text(windows,width=100,height=10)
    text.pack()
    masage = entry.get()
    for group in selected_list:
        for person in user.get_person_list(group=group):
            qqhao = user.send_masage(person, masage)
            if qqhao:
                text.insert(tk.END,qqhao + " " + time.strftime("%Y-%m-%d %H:%M:%S") + ":" + masage+  "\n")
                time.sleep(0.5)
                #添加之后，立即更新
                windows.update()

    user.stop()

def main():
    threading.Thread(target=saomiao).start()
    windows.geometry("1000x900+0+0")
    tk.Label(windows, text="①请使用手机扫描授权登陆！").pack()

    img = tk.PhotoImage(file="erweima.png")
    label = tk.Label(windows, image=img)
    label.pack()
    windows.mainloop()

if __name__ == '__main__':
    main()
