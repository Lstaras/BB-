#coding=utf-8
import time 
from selenium import webdriver#导入库

#读取答案库
f = open("unit8.txt","r",encoding="utf-8")   #设置文件对象
filelines = f.readlines()

data = {}

for fileline in filelines:
    #print(fileline)
    t = fileline.split('|')
    t[1] = t[1].strip('\n')
    print(t)
    data[t[0]] = t[1]

print(data)
f.close() #关闭文件

#网络部分
browser = webdriver.Chrome()#声明浏览器

user_id = ''
password = ''

url = 'https://bb.btbu.edu.cn/'
browser.get(url)#打开浏览器预设网址
time.sleep(2)#延时加载

#登录
try:
    browser.find_element_by_id('user_id').send_keys(user_id)
    browser.find_element_by_id('password').send_keys(password)
    #模拟点击登录
    browser.find_element_by_xpath("//*[@id='login']").click()
    time.sleep(2)
    print("login success")
except:
    print("login failed")

#进入答题页面
url2 = ''
browser.get(url2)
browser.find_element_by_name('bottom_开始').click()
time.sleep(2)

#进入新答题页面
url3 = ''
browser.get(url3)
time.sleep(2)

# 提交class="abutton pagelink"
# 词汇class="vtbegenerated inlineVtbegenerated"
# 输入id="fitb-ans-XXX"
#答题
for i in range(59):
    time.sleep(5)
    word = browser.find_element_by_xpath("//*[@class='vtbegenerated inlineVtbegenerated']").text
    print(word)
    ans = data[word]
    print(ans)
    browser.find_element_by_xpath('//*[starts-with(@id,"fitb-ans")]').send_keys(ans)
    time.sleep(1)
    browser.find_element_by_xpath("//*[@class='abutton pagelink']").click()

browser.close()




