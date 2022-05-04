from selenium import webdriver
 
browser = webdriver.Chrome()
 
browser.get("http://www.baidu.com")
 
browser.find_element_by_id("kw").send_keys("selenium")  #F12檢視到的www.baidu.com的輸入框的Id是“kw”,通過id找到該元素後，輸入“selenium”字串
browser.find_element_by_id("su").click()   #F12檢視到的www.baidu.com的submit的Id是“su”，通過id找到該元素後，執行點選事件
 
browser.quit()