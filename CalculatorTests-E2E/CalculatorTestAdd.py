from selenium import webdriver
import time
import selenium.webdriver.support.ui as UI

driver = webdriver.Chrome()
# Open the webpage
driver.get('http://juliemr.github.io/protractor-demo/')

first_number = driver.find_element_by_css_selector('[ng-model=first]')
first_number.send_keys('2')
second_number = driver.find_element_by_css_selector('[ng-model=second]')
second_number.send_keys('3')
operation_add = UI.Select(driver.find_element_by_css_selector('[ng-model=operator]')).select_by_value("ADDITION")
result_button = driver.find_element_by_class_name('btn')
result_button.click()
result = driver.find_elements_by_tag_name('h2')
time.sleep(5)
assert result == '5'