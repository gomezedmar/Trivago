'''
Created on 26 de jun de 2017

@author: vntedsi
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Firefox()
driver.delete_all_cookies()
#Opens the  requested URL
driver.get("https://trivago.com.br")
driver.find_element_by_xpath(".//input[@type='search']").send_keys("Campi")
driver.find_element_by_xpath(".//*[@class='horus-btn-search__label']").click()
driver.implicitly_wait(3)
driver.find_element_by_partial_link_text("Campinas").click()
driver.find_element_by_xpath(".//div[@class='horus__col horus__col--checkin']").click()
driver.find_element_by_css_selector("button.cal-btn-next").click()
driver.find_element_by_css_selector("button.cal-btn-next").click()
driver.find_element_by_css_selector("button.cal-btn-next").click()

