import time

import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from taobaosetting import *
from urllib.parse import quote

chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser=webdriver.Chrome(chrome_options=chrome_options)

wait=WebDriverWait(browser,10)
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]
def login():
    browser.get(login_url)
    try:
        btn1= wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')))
        btn1.click()
        btn2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_OtherLogin > a.weibo-login')))
        btn2.click()
    except TimeoutException:
        btn2 =wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_OtherLogin > a.weibo-login')))
        btn2.click()
    usr_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(2) > div > input')))
    pawd_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(3) > div > input')))
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a')))
    usr_input.send_keys(weibo_user)
    pawd_input.send_keys(weibo_pawd)
    submit.click()
def search(keyword):
    input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
    submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
    input.send_keys(keyword)
    submit.click()
    parse_page_detail(ISToDB)
def index_page(keyword,index):
    try:
        if index==1:
            search(keyword)
        else:
            index_input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
            index_input.clear()
            index_input.send_keys(index)
            submit.click()
            highlight_span=wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(index)))
            parse_page_detail(ISToDB)
    except TimeoutException:
        index_page(keyword, index)
def parse_page_detail(ISToDB=False):
    html=browser.page_source
    doc=pq(html)
    items=doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product={
            'name':item.find('.title').text(),
            'price':item.find('.price strong').text(),
            'dealCount':item.find('.deal-cnt').text(),
            'shop':item.find('.shop').text(),
            'location': item.find('.location').text(),
        }
        print(product)
        if ISToDB:
            save_to_mongo(product)
    time.sleep(2)

def save_to_mongo(result):
    try:
        if db[KEYWORD].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')
def main():
    login()
    for i in range(1,10):
        index_page(KEYWORD,i)
if __name__=='__main__':
    main()