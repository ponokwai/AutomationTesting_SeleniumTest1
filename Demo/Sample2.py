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
driver.find_element_by_css_selector("li.nav-item:nth-child(1) > a:nth-child(1)")
time.sleep(3)
