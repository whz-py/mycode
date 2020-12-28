import time
import re

from pyquery import PyQuery as pq
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pymongo import MongoClient
from mongo import *

mongo = MongoClient(MONGO_URL)
db = mongo[MONGO_DB]


# browser = webdriver.Firefox()

# 这里用firefox的无头模式
firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-gpu")
browser = webdriver.Firefox(options=firefox_options)
wait = WebDriverWait(browser, 5)


def search(keyword):
    try:
        browser.get("https://www.jd.com/")
        # 输入需要爬取的商品
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        # 这是搜索按钮
        button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search > div > div.form > button')))
        input.send_keys(keyword)
        # 点击搜索按钮
        button.click()
        # 等待页数的加载
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b')))
        # 页码全部加载出来后，调用获取商品信息的函数
        print("正在获取第1页数据")
        get_product()
        # print(total.text)
        return total.text
    except TimeoutException:
        return search(keyword)


def pull_page_to_bottom():
    js = 'return action = document.body.scrollHeight'
    # 初始高度
    height = browser.execute_script(js)
    # print(height)
    # 将页面滚动到当前的页面底部
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    # 定义初始时间
    t1 = int(time.time())
    # 重复次数
    num = 0
    while True:
        t2 = int(time.time())
        if t2 - t1 < 5:
            new_height = browser.execute_script(js)
            if new_height > height:
                time.sleep(1)
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
                height = new_height
                t1 = int(time.time())
        # 当页面超过10秒没有更新时，进入重试逻辑，重试2次
        elif num < 2:
            time.sleep(1)
            num += 1
        else:
            print("已经在最下方")
            break


def get_next_page(i):
    try:
        print("正在获取第{}页数据".format(i))
        page_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.input-txt:nth-child(2)')))
        # 等到确定按钮可以点击的时候
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.btn:nth-child(4)')))
        # time.sleep(3)
        # 清空输入框里的页码
        page_input.clear()
        # 填入页码i
        page_input.send_keys(i)
        # time.sleep(1)
        # 点击确定按钮，翻页
        submit.click()
        time.sleep(1)
        pull_page_to_bottom()
        get_product()
    except TimeoutException:
        get_next_page(i)

def get_product():
    # 等到页面加载成功时
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-list #J_goodsList .gl-item')))
    html = browser.page_source
    # 用pyquery解析页面
    doc = pq(html)
    items = doc('.m-list #J_goodsList .gl-item').items()
    for item in items:
        product = {
            "title": item.find('.p-name').text(),
            "price": item.find('.p-price').text(),
            "comment_counts": item.find('.p-commit').text(),
            "image": item.find('.p-img').attr('src'),
            "shop": item.find('.p-shop .J_im_icon').text()
        }
        print(product)
        # save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert_one(result):
            print("存储到mongodb成功", result)
    except Exception:
        print("存储到mongodb失败", result)

def main():
    keyword = input("请输入需要爬取的商品关键字：")
    total = search(keyword)
    try:
        page_num = int(total)
        for i in range(2, page_num + 1):
            get_next_page(i)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()




