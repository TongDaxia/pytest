# -*- coding:utf-8 -*-

# douban.py
#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions 类，负责条件出发
from selenium.webdriver.support import expected_conditions as EC


chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')

class Douban():
    def __init__(self):
        self.url = "https://www.douban.com/"
        #self.driver = webdriver.PhantomJS()
        self.driver = webdriver.Chrome(chrome_options=chrome_option)

    def log_in(self):
        self.driver.get(self.url)
        time.sleep(3)#睡3分钟，等待页面加载
        self.driver.save_screenshot("0.png")
        #输入账号
        #self.driver.find_element_by_xpath('//*[@id="form_email"]').send_keys("664609506@qq.com")


        #  /html/body/div[1]/div[1]/ul[1]/li[2]
        # 模拟点击一下这个按钮
        # 在 ac 位置单击
        ac = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul[1]/li[2]")
        ActionChains(self.driver).move_to_element(ac).click(ac).perform()

        try:
            print("**********")
            # 页面一直循环，直到 id="myDynamicElement" 出现
            element1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
        finally:
            self.driver.quit()
        element1.send_keys("664609506@qq.com")
        #输入密码
        # self.driver.find_element_by_xpath('//*[@id="form_password"]').send_keys("t4646464646yg")

        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("t4646464646yg")
        #点击登陆
        self.driver.find_element_by_class_name("bn-submit").click()
        time.sleep(2)
        self.driver.save_screenshot("douban.png")
        #输出登陆之后的cookies
        print(self.driver.get_cookies())

    '''def __del__(self):
        调用内建的稀构方法，在程序退出的时候自动调用
        类似的还可以在文件打开的时候调用close，数据库链接的断开
        
        self.driver.quit()
    '''
if __name__ == "__main__":
    douban = Douban() #实例化
    douban.log_in() #之后调用登陆方法