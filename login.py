import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service 
import chromedriver_autoinstaller 
chromedriver_autoinstaller.install() 

#username = "j48072035"
#password = "JimboTronWhoo"

def login(user, passw):

    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument('--user-agent="Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1"')

    driver = webdriver.Chrome(options=options)
    url = "https://twitter.com/i/flow/login"
    driver.get(url)

    username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
    username.send_keys(user)
    username.send_keys(Keys.ENTER)

    try:
        username_again = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="text"]')))
        username_again.send_keys(user)
        username_again.send_keys(Keys.ENTER)
    except:
        pass



    password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    password.send_keys(passw)
    password.send_keys(Keys.ENTER)

    return driver

