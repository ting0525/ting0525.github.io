from typing import KeysView
from selenium import webdriver

#瀏覽器啟動設置類
PATH = "C:/Users/j0918/Desktop/chromedriver/chromedriver.exe"

optons=webdriver.ChromeOptions()

#瀏覽器啟動配置

optons.add_argument('disable-infobars')

#啟動谷歌瀏覽器

driver=webdriver.Chrome(PATH)

#最大化窗口

driver.maximize_window()

#打開網址

driver.get("https://www.dcard.tw/f")
search = driver.find_element_by_name("query")
search.send_keys("比特")

search.send_keys(KeysView.RETURN)

