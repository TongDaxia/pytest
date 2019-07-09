from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

#调用环境变量指定的PhantomJS 浏览器创建浏览器对象
#driver = webdriver.PhantomJS()

# 如果没有在环境变量指定PhantomJS位置
#driver = webdriver.PhantomJS(executable_path="D:/tools/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver = webdriver.Chrome(executable_path="D:/tools/chromedriver.exe")

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
time.sleep(2)
driver.get("http://www.baidu.com/")

data = driver.find_element_by_id("wrapper").text

print(data)

