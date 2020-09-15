from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome(r"C:\Users\Patrick.Onokwai\PycharmProjects\SeleniumProject2\Browsers\chromedriver.exe")
#driver = webdriver.Chrome()
# driver = webdriver.Firefox()
#driver=webdriver.ie()
#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and enter the value
driver.find_element_by_css_selector(".gLFyf").send_keys("javapoint")
#driver.find_element_by_class_name('q').send_keys("javapoint")
time.sleep(3)
#click on the search button
driver.find_element_by_name("btnK").click()
time.sleep(3)
#close the browser
driver.close()
print("sample test was successfully complete")