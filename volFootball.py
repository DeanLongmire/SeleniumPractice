from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = Chrome(chrome_options=opts)

driver.get("https://www.sports-reference.com/cfb/schools/tennessee/2022.html")

roster = driver.find_element(By.XPATH, '//*[@id="inner_nav"]/ul/li[4]/a')
roster.click()

time.sleep(5) #lets the page load

roster = driver.find_element(By.TAG_NAME, "tbody")

tableElements = roster.find_elements(By.TAG_NAME, "tr")

time.sleep(5)

for tableElement in tableElements:
    rows = tableElement.find_elements(By.TAG_NAME, "td")
    for row in rows:
        print(row.text)



    




