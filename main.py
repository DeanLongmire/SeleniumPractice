from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome

PATH = "C:\Program Files (x86)\chromedriver.exe"

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = Chrome(chrome_options=opts)

driver.get("https://www.sports-reference.com/cfb/schools/tennessee/2022.html")


