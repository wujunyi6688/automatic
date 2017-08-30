########################################
########第一个网页自动化脚本############
########################################
from selenium import webdriver
import time

browser = webdriver.Firefox()                              #定义火狐浏览器
browser.get("http://www.baidu.com")                        #输入访问网址并回车
browser.maximize_window()
browser.set_window_size(400,600)
time.sleep(2)
# browser.find_element_by_id("kw").send_keys("自动化测试")   #向id为kw的输入框填充之
# browser.find_element_by_id("su").click()                   #点击id为su的按钮控件
browser.find_element_by_link_text('贴吧').click()
time.sleep(6)                                              #等待6S
browser.find_element_by_id('wd1').send_keys("中印冲突")
browser.find_element_by_link_text('全吧搜索').click()
browser.implicitly_wait(10)                                #智能等待10s（最长10s,响应完成即可不用等待）
browser.quit()                                             #退出浏览器