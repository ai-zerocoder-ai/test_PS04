# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# выйти из программы.

from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

text = input('введите запрос: ')

browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/')
time.sleep(5)

assert "Википедия" in browser.title
time.sleep(5)

search_box = browser.find_element(By.ID, 'searchInput')
search_box.send_keys(text)
search_box.send_keys(Keys.RETURN)
time.sleep(5)

a = browser.find_elements(By.LINK_TEXT, text)
a[0].click()
time.sleep(5)





browser.quit()
