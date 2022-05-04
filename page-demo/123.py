from selenium import webdriver
PATH = "C:/Users/j0918/Desktop/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('http://www.google.com/')
#開啟首頁

driver.implicitly_wait(6)
#等待網站載入(最多等6秒

driver.find_element_by_xpath('//*[@id="gbw"]/div/div/div[1]/div[2]/a').click()