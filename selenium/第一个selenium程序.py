from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
option = webdriver.ChromeOptions()
option.add_argument('--user-agent=iphone')
driver = webdriver.Chrome(chrome_options=option)
driver.get('https://qzone.qq.com/')

time.sleep(3)
#
username = driver.find_element_by_id("u")
password = driver.find_element_by_id("p")
login = driver.find_element_by_id("go")

username.send_keys("2403818207")
password.send_keys("ppp250941")

login.click()
time.sleep(3)

withme = driver.find_element_by_id("nav_bar_me")
withme.click()
time.sleep(1)

zhuye = driver.find_element_by_id("nav_bar_main")
zhuye.click()

time.sleep(1)

# shuoshuo_list = driver.find_element_by_css_selector("div.feed.dataItem")
shuoshuo= driver.find_element_by_class_name("source")
ActionChains(driver).click(shuoshuo).perform()
#
# print(shuoshuo_list)

#
# shuoshuo_list.click()

# for shuoshuo in shuoshuo_list:
#     shuoshuo.click()
#     print(shuoshuo)
#     time.sleep(1)
# print(shuoshuo_list[1])

# button = driver.find_element_by_class_name("bn")
# content.send_keys("pengzuyu")
#
# button.click()

# driver.quite()