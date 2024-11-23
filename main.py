from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

text = input('введите запрос: ')

browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/')
time.sleep(3)

assert "Википедия" in browser.title

search_box = browser.find_element(By.ID, 'searchInput')
search_box.send_keys(text)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

a = browser.find_element(By.LINK_TEXT, text)
a.click()
time.sleep(3)

ask = input('выберите действие (1 - листать параграфы, 2 - перейти на внутренние статьи, 3 - выход): ')

if ask == '1':
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    for para in paragraphs:
        print(para.text)
        input('Нажмите Enter, чтобы перейти к следующему параграфу...')
elif ask == '2':
    links = browser.find_elements(By.CSS_SELECTOR, 'a[href]')
    if links:
        random_link = random.choice(links)  # Случайный выбор ссылки
        selected_link = random_link.get_attribute('href')
        print(f"Переход по случайной ссылке: {random_link.text} ({selected_link})")
        browser.get(selected_link)
        time.sleep(3)

        ask2 = input('выберите действие (1 - листать параграфы, 2 - выход): ')
        if ask2 == '1':
            paragraphs = browser.find_elements(By.TAG_NAME, 'p')
            for para in paragraphs:
                print(para.text)
                input('Нажмите Enter, чтобы перейти к следующему параграфу...')
        elif ask2 == '2':
            browser.close()
    else:
        print("Ссылки не найдены.")
elif ask == '3':
    browser.close()
else:
    print("Некорректный выбор.")
    browser.close()
