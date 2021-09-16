#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time


driver = webdriver.Opera(executable_path=r"C:\Users\Student\Downloads\operadriver.exe")
driver.get("https://dominos.com/en/")

time.sleep(10)

click_delivery = driver.find_element_by_xpath('//*[@id="homeWrapper"]/main/section[1]/div/div[2]/a[2]')
click_delivery.click()

time.sleep(10)

driver.find_element_by_xpath('//*[@id="Postal_Code_Sep"]').click()
#equivalent to left clicking on text field
# fill in field with zipcode
driver.find_element_by_xpath('//*[@id="Postal_Code_Sep"]').send_keys('98499' + Keys.RETURN)

time.sleep(10)

driver.find_element_by_xpath('//*[@id="locationsResultsPage"]/div/div[2]/div[1]/div[2]/div/div[2]/div/a').click()

time.sleep(10)

driver.find_element_by_xpath('//*[@id="entree-Pizza"]/a/div[2]/h2').click()

time.sleep(10)

driver.find_element_by_xpath('//*[@id="categoryPage2"]/section/div/div[3]/div/a[2]').click()

time.sleep(10)

driver.find_element_by_xpath('//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/div[2]/button').click()

time.sleep(10)

driver.find_element_by_xpath('//*[@id="pizzaBuilderPage"]/div[3]/div[5]/div[1]/div[2]/button').click()

time.sleep(10)
