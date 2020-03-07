from selenium import webdriver
import os
import sys

EMAIL = 'kyahata.america@gmail.com'
PASSWORD = '08220810Ak'
Product = 'Logitech G520'
#PRODUCT = str(sys.argv[1]).replace(' ', '+')
#url = 'https://www.amazon.com/s?k=' + PRODUCT + '&ref=nb_sb_noss_2'

driver = webdriver.Chrome('/Users/hachimannoboruju/Documents/Python/Project/Selenium/chromedriver')

def getPrice():
    driver.get('https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&switch_account=')
    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys(EMAIL)
    driver.find_element_by_xpath('//*[@id="continue"]').submit()

    driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys(PASSWORD)
    driver.find_element_by_xpath('//*[@id="signInSubmit"]').submit()

    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(Product)
    driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a')[0].click()

if __name__ == '__main__':
    getPrice()