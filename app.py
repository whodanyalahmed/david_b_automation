
from ast import Try
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from config import *

# make chrome headless function
def chrome(headless=False):
    # add fake user agent
    chrome_options = Options()

    # return webdriver
    # support to get response status and headers
    d = webdriver.DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'performance': 'ALL'}

    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("user-agent={}".format(
    #     fake_useragent.UserAgent().random))
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(
        executable_path=r'i://clients//chromedriver.exe', options=chrome_options, desired_capabilities=d)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


driver = chrome()

driver.maximize_window()

try:
    driver.get('https://prenotami.esteri.it/Services')
    print("info: page loaded")
except Exception as e:
    print(e)
    print("error: page not loaded")         # print error message


def login():
    try:
        driver.find_element_by_id('login-email').send_keys(email)
        print("info: email entered")
    except Exception as e:
        print(e)
        print("error: email not entered")
    try:
        driver.find_element_by_id('login-password').send_keys(password)
        print("info: password entered")
    except Exception as e:
        print(e)
        print("error: password not entered")
    try:
        driver.find_element_by_xpath('button[@data-sitekey="6LdSmG4cAAAAAOarRxGIhehvv4sPgVeF-vRi-Jqb"]').click()
        print("info: login button clicked")
    except Exception as e:
        print(e)
        print("error: login button not clicked")


login()
