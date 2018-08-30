from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
option = webdriver.ChromeOptions()
# option.add_argument('--headless')
# option.set_headless()
print("设置完成浏览器属性")
driver = webdriver.Chrome("C:\ProgramData\Anaconda3\Scripts\chromedriver.exe",chrome_options=option)
driver.set_window_size(1920, 1080)


option.add_argument('lang=zh_CN.UTF-8')
driver.get("https://www.weibo.com/hk")
driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("1507133197")
driver.find_element_by_name("password").send_keys("wU19970119@")
driver.find_element_by_css_selector(".W_btn_a.btn_32px").click()
time.sleep(5)
try:
    driver.find_element_by_xpath("//img[@action-type='btn_change_verifycode']")
except:
    print("无验证码")
else:
    print("有验证码")
time.sleep(5)
