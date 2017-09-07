########################################
########第一个网页自动化脚本############
########################################
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()                              #定义火狐浏览器
browser.get("http://www.baidu.com")                        #输入访问网址并回车
browser.maximize_window()                                  #最大化浏览器的窗口
#browser.set_window_size(400,600)                           #设定浏览器的长宽
time.sleep(2)
# browser.find_element_by_id("kw").send_keys("自动化测试") #向id为kw的输入框填充之
# browser.find_element_by_id("su").click()                 #点击id为su的按钮控件
browser.find_element_by_link_text('贴吧').click()
time.sleep(6)                                              #等待6S


#对浏览器做前进后退操作
browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)

#防止中文输入乱码，使用utf-8或者gbk编码
#coding = utf-8或gbk
browser.find_element_by_id('wd1').send_keys(u"中印冲突")

#键盘回车操作
#browser.find_element_by_id('passw').send_keys(Keys.ENTER)

browser.find_element_by_link_text('全吧搜索').click()
browser.implicitly_wait(10)                                #智能等待10s（最长10s,响应完成即可不用等待）
browser.quit()                                             #退出浏览器








##########鼠标点击操作############
#定位点击对象
button1 = browser.find_element_by_id('tab')
target = browser.find_element_by_id('tar')

#获取所定义的浏览器，对定位出的对象实行右击处理
ActionChains(browser).context_click(button1)

#获取所定义的浏览器，对定位出的对象实行双击处理
ActionChains(browser).double_click(button1)

#获取所定义的浏览器，对定位出的对象拖动到目标对象位置
ActionChains(browser).drag_and_drop(button1,target)