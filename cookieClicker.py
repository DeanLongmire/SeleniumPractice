from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = Chrome(chrome_options=opts)

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

languageSelect = driver.find_element(By.ID, "langSelect-EN")
languageSelect.click()

time.sleep(3)

acceptCookies = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
acceptCookies.click()

cookie = driver.find_element(By.ID, "bigCookie")
cookieCount = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, ("productPrice" + str(i))) for i in range(1,-1,-1)]

while(1):
    cookie.click()
    count = int(cookieCount.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()






