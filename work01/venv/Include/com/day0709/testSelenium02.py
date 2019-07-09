from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import  Keys
#导入 ActionChains 类
from selenium.webdriver import ActionChains
import time
#导入 ActionChains 类
from selenium.webdriver import ActionChains

chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_option)

driver.get('http://www.baidu.com')

data = driver.find_element_by_id("wrapper").text

# print(data)
print(driver.title)
# 生成当前页面快照并保存
driver.save_screenshot("baidu.png")
driver.find_element_by_id("kw").send_keys(u"长城")
driver.find_element_by_id("su").click()

driver.save_screenshot("长城.png")
time.sleep(2)
# 获取新的页面快照
driver.save_screenshot("长城1.png")

print("源代码:",driver.page_source)
print ("cookies:",driver.get_cookies())

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# 输入框重新输入内容
driver.find_element_by_id("kw").send_keys("合肥")
# 模拟Enter回车键
driver.find_element_by_id("su").send_keys(Keys.RETURN)

# 清除输入框内容
# 生成新的页面快照
driver.save_screenshot("合肥.png")
time.sleep(2)
driver.find_element_by_id("kw").clear()
driver.save_screenshot("合肥1.png")
# 获取当前url
print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()


# 关闭浏览器
driver.quit()