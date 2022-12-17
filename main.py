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



    




