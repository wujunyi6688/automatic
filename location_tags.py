from selenium import webdriver
import time
import os

#点击查看总金额的按钮，触发js函数统计总金额输出
def add_btn():
    button = br.find_element_by_name("btn")
    button.click()
    time.sleep(3)
#点击全选按钮一次或者两次，清空所选项
def clear_box(b):
    all = br.find_element_by_name('all')
    all.click()
    if(b>0):
        all.click()

def result_clear(a):
    add_btn()
    time.sleep(1)
    clear_box(a)
    time.sleep(1)


br = webdriver.Chrome()
#获取本地访问的html文件
local_path = 'file:///'+os.path.abspath('checkbox.html')
br.get(local_path)


#获取所有的input标签对象，并筛选type为checkbox的对象加以点击勾选
inputs = br.find_elements_by_tag_name("input")
for input in inputs:
    if(input.get_attribute("type") == "checkbox" and input.get_attribute("name") != "all"):
        input.click()
        time.sleep(1)
    pass

pass
result_clear(0)


for input in inputs:
    if(input.get_attribute("type") == "checkbox" and input.get_attribute("name") == "all"):
        input.click()
        time.sleep(1)
    pass
pass
result_clear(0)

index = 0
pass
for input in inputs:
    if(input.get_attribute("type") == "checkbox" and (index == 2 or index == 3)):
        input.click()
        time.sleep(1)
    index = index + 1
    pass
pass
result_clear(1)

br.quit()




