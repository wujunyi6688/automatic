from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys

br = webdriver.Chrome()
#获取本地访问的html文件
local_path = 'file:///'+os.path.abspath('frame.html')
br.get(local_path)

#由于需要定位的控件处于frame.html里面的frame1框架中（src=inner.html）中的frame2框架，所以需要浏览器进入框架内部
br.switch_to_frame("f1")
br.switch_to_frame("f2")

br.find_element_by_id("kw").send_keys(u"Python语言")
time.sleep(1)

#回车操作，避免百度的匹配队列把定位控件遮住
br.find_element_by_id('kw').send_keys(Keys.ENTER)
#br.find_elements_by_id("su")
time.sleep(3)
#进行返回操作，点击“新闻”链接
#br.back()
br.find_element_by_link_text(u"新闻").click()
time.sleep(3)
br.quit()




time.sleep(3)
br.quit()