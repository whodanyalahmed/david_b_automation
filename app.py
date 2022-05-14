
from ast import Try
import time
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


def home():

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
        # click button that contains text "Avanti"
        driver.find_element_by_xpath('//*[contains(text(), "Avanti")]').click()
        print("info: login button clicked")
    except Exception as e:
        print(e)
        print("error: login button not clicked")


def process():
    try:
        # click on button with link /Services/Booking/345
        driver.find_element_by_xpath(
            '//a[@href="/Services/Booking/345"]').click()
        print("info: booking button clicked")
    except Exception as e:
        print(e)
        print("error: booking button not clicked")
    # scroll to last
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")
    try:
        # click on button with text "Prenota"
        time.sleep(3)
        cb = driver.find_element_by_xpath('//input[@id="PrivacyCheck"]')
        driver.execute_script("arguments[0].click();", cb)
        print("info: privary checkbox clicked")
    except Exception as e:
        print(e)
        print("error: privary checkbox not clicked")
    # click on button with text "Avanti"
    try:
        driver.find_element_by_xpath('//*[contains(text(), "Avanti")]').click()
        print("info: next button clicked")
    except Exception as e:
        print(e)
        print("error: next button not clicked")
    alert = driver.switch_to.alert
    try:
        alert.accept()  # If you want to Accept the Alert
        print("info: alert accepted")
    except:
        alert.dismiss()  # If  You want to Dismiss the Alert.
    # alert.dismiss()
        print()
    # click on button with text "ok"
    try:
        driver.find_element_by_xpath(
            '//html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button').click()
        print("info: ok button clicked")
    except Exception as e:
        print(e)
        print("error: ok button not clicked")
    # stop the script
    driver.quit()


def main():

    home()
    login()
    home()
    process()


main()
