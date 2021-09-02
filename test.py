from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.sportybet.com/ng/')
time.sleep(10)
driver.find_element_by_link_text('/ng/sport/football').click()
time.sleep(10)