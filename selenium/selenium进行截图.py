#定位有误差，原因未找出 x相差247 y相差59
from selenium import webdriver
from PIL import Image

broswer = webdriver.Chrome()
broswer.maximize_window()
broswer.get("http://www.baidu.com")
broswer.save_screenshot(r'baidu.png')
baidu = broswer.find_element_by_id('su')
left = baidu.location['x'] + 247
top = baidu.location['y'] + 59
elementWidth = baidu.location['x'] + baidu.size['width']
elementHeight = baidu.location['y'] + baidu.size['height']
picture = Image.open(r'baidu.png')
picture = picture.crop((left, top, elementWidth, elementHeight))
picture.save(r'baidu2.png')
broswer.quit()