from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://qzone.qq.com/")

time.sleep(1)

driver.switch_to_frame('login_frame')
change = driver.find_element_by_id("switcher_plogin")
change.click()

username = driver.find_element_by_id("u") #driver.find_element_by_id("nav_bar_me")
password = driver.find_element_by_id("p")
login_bt = driver.find_element_by_id("login_button")


username.send_keys("2403818207")
password.send_keys("ppp250941")

login_bt.click()
time.sleep(1)


my_zhuye = driver.find_element_by_id("aMainPage")
my_zhuye.click()
time.sleep(1)

my_shuoshuo = driver.find_element_by_id("QM_Profile_Mood_A")
my_shuoshuo.click()
time.sleep(4)

# js = 'div_list = document.getElementsByClassName("dropdown-menu"); for(i = 0;i < div_list.length;i++){ console.log(div_list[i]);div_list[i].style.display = "block";}'
# driver.execute_script(js)
driver.switch_to_frame('app_canvas_frame')
div_list = driver.find_elements_by_css_selector(".dropdown-trigger.c_tx")
aaa = 0
while 1:
        # try:
        #     driver.switch_to_frame('app_canvas_frame')
        #     div = driver.find_element_by_css_selector(".dropdown-trigger.c_tx")
        # except:
        #     print("1")
        #     driver.switch_to_default_content()
        #     continue
        aaa+=1
        div = div_list[aaa]
        div.click()
        time.sleep(2)
        del_bt = driver.find_element_by_css_selector(".del.del_btn.author_display")
        print(del_bt)
        del_bt.click()
        time.sleep(2)
        driver.switch_to_default_content()
        current_bt = driver.find_element_by_css_selector(".qz_dialog_layer_btn.qz_dialog_layer_sub")
        current_bt.click()
        time.sleep(4)
    # next_page = driver.find_element_by_id("pager_next_2")
    # next_page.click()
    # time.sleep(6)

driver.quit()


