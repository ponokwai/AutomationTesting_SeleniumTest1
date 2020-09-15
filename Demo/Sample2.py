from selenium import webdriver
import time

print("Completing formy application")

#get driver
driver = webdriver.Chrome()
driver.maximize_window()
# navidate to url
driver.get("https://formy-project.herokuapp.com/")

time.sleep(3)
#click on form
driver.find_element_by_css_selector("li.nav-item:nth-child(1) > a:nth-child(1)").click()
time.sleep(3)
driver.find_element_by_css_selector("#first-name").send_keys("Patrick")
driver.find_element_by_css_selector("#last-name").send_keys("Onokwai")
driver.find_element_by_css_selector("#job-title").send_keys("Software Engineer")
driver.find_element_by_css_selector("#radio-button-3").click()
driver.find_element_by_css_selector("div.input-group:nth-child(9) > div:nth-child(2)").click()
driver.find_element_by_css_selector("#select-menu > option:nth-child(5)").click()
driver.find_element_by_css_selector("#checkbox-1").click()
driver.find_element_by_css_selector("#datepicker").click()
driver.find_element_by_css_selector("td.today").click()

time.sleep(5)
driver.find_element_by_css_selector(".btn").click()
time.sleep(3)
driver.close()