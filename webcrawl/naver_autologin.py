from selenium import webdriver
from bs4 import BeautifulSoup
ctx ='../crawler/chromedriver'
driver = webdriver.Chrome(ctx)
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
driver.find_element_by_name('id').send_keys('01099473080')
driver.find_element_by_name('pw').send_keys('wkfkd123@')

driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.implicitly_wait(3)