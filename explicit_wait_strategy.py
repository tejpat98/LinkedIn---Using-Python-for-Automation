from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from time import sleep

url = "https://the-internet.herokuapp.com/dynamic_controls"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get(url)

#The webdriver will wait 10 seconds for the condition to be met before moving to the next step
wait = WebDriverWait(driver, 10)

# Explicit waits are when the script waits for a condition to be met before continuing
# Implicit waits are when the script waits for a pre-defined amount of time

# checkbox = driver.find_element(By.XPATH, '//*[@id="checkbox"]/input')
# checkbox_rem = driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
# txt_field = driver.find_element(By.XPATH, '//*[@id="input-example"]/input')

txt_enable = driver.find_element(By.XPATH, '//*[@id="input-example"]/button')
sleep(0.5)
txt_enable.click()
txt_disable = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="input-example"]/button')))
sleep(0.5)
txt_disable.click()

#Pause the script to view for 5 seconds
sleep(5)

#close browser window and quit driver
driver.quit()