from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

url = "http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get(url)

washington = driver.find_element(By.XPATH, '//*[@id="box3"]')
usa = driver.find_element(By.XPATH, '//*[@id="box103"]')

actions = ActionChains(driver)
# Perform a drag and drop, dragging 'washington' to 'usa'
actions.drag_and_drop(washington, usa).perform()

#Pause the script to view for 5 seconds
sleep(5)

#close browser window and quit driver
driver.quit()