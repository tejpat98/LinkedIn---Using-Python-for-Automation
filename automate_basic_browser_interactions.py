from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get(url)

#Find First Name field, input text "Tejash"
first_name = driver.find_element(By.XPATH, '//*[@id="input-firstname"]')
first_name.send_keys("Tejash")

#Click "No" for subscribing to news letters
newsletter_sub = driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/div[2]/label')
newsletter_sub.click()

#Pause the script to view for 5 seconds
sleep(5)

#close browser window and quit driver
driver.quit()