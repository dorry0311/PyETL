from selenium.webdriver import Chrome
import requests
url = 'https://www.ptt.cc/bbs/index.html'
driver = Chrome('./chromedriver.exe')
driver.get(url)
driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()
print(driver.get_cookies())
cookie_list = driver.get_cookies()

driver.close()

ss = requests.session()

for i in cookie_list:
    ss.cookies.set(i['name'],i['value'])
res = ss.get('https://www.ptt.cc/bbs/Gossiping/index.html')
print(res.text)