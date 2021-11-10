'''
作者：梦里北极光
时间：2021/11/09
功能：设置时间，定时自动化抢购淘宝商品，此脚本最适合双十一抢购商品
感受：基本使用循环语句，反正是脚本，只求功能不求规范哈

'''


#导入时间模块
import datetime
import time
#import webbrowser
#brower=webbrowser.open("https://www.taobao.com")
from selenium import webdriver

print("亲，请输入需要定时抢购的时间，格式如双十一时间：2021-11-11 00:00:00.00000000")
times = input()
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#now1 =datetime.datetime.now()
print("亲,目前时间是"+now)
#print(now1)
#如果没有设置环境变量，可使用导入谷歌程序的地址
#option = webdriver.ChromeOptions()
#option.binary_location = r'"C:\Users\AppData\Local\Google\Chrome\Application\chrome.exe"'
#打开谷歌浏览器
brower = webdriver.Chrome()
#访问浏览器淘宝网站
brower.get("https://www.taobao.com")
#找到页面登录界面点击登录
brower.find_element_by_link_text("亲，请登录").click()
print("亲，请尽快扫码登陆哦！")

num = 0
#账号登录等待中
while True:
    try:
       if brower.find_element_by_link_text("短信登录"):
            time.sleep(1)
            num = num+1
            print("账号密码登录中。。。已等待" + str(num) + "秒")
    except:
        print("正在跳转二维码页面。。。")
        break
#重新赋值
num = 0
#扫码登录界面等待中
while True:
    try:
       if brower.find_element_by_class_name("master-login-title"):
            time.sleep(1)
            num = num+1
            print("扫码登录中。。。已等待" + str(num) + "秒")
    except:
        print("正在跳转已登录界面")
        break


#进入购物车页面
brower.get("https://cart.taobao.com/cart.htm")
print("已进入购物界面，即将自动勾选商品！")
#勾选全选购物车
while True:
    try:
        if brower.find_element_by_id("J_SelectAll1"):
            #勾选购物车
            brower.find_element_by_id("J_SelectAll1").click()
            print("已全选商品，即将等待双十一，进行结算")
            break
    except:
        time.sleep(1)
        print("找不到购买按钮，或者未进入购物界面")

#设置抢购时间也就是双十一时间
#times = "2021-11-11 00:00:00.00000000"
#进行结算，如果到达抢购时间进行结算

while True:
    try:
        # 获取电脑时间
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print("现在时间为" + now + "等待双十一抢购等待中。。。。")
        # 判断时间是否到达抢购时间
        # 等待刷新时间
        time.sleep(0.01)
        if now >= times:
            print("时间到，进入结算中。。。。")
            break
    except:
        print("继续等待")
        pass

#进行循环结算
while True:
    try:
        if brower.find_element_by_link_text("结 算"):
            brower.find_element_by_link_text("结 算").click()
            print("已点击结算，即将跳转提交界面中，请保持网络正常。。。")
            #time.sleep(2)
            break
        else:
            time.sleep(1)
            print("等待1秒未结算，正努力结算中！")
    except:
        # time.sleep(1)
        print("结算失败！刷新中。。。")
        break
        #进入结算界面循环进行提交订单

#进行循环提交订单
num1=0
while True:
    num1 = num1+1
    try:
        if brower.find_element_by_link_text("提交订单"):
            brower.find_element_by_link_text("提交订单").click()
            print("抢购成功，亲，请尽快付款，快快快")
            break
        else:
            print("未提交订单，正努力提交中！")
    except:
        print("提交失败！刷新中。。。第"+str(num1)+"次！")
        pass
print("本次服务到此结束，欢迎关注锤子研究所！")








