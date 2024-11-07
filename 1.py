from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
# Search for "selenium"
search_box = driver.find_element_by_name("q")
search_box.send_keys("selenium")
search_box.send_keys(Keys.RETURN)
sleep(5)

driver.quit()