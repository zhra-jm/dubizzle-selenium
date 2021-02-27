from time import sleep

from selenium import webdriver


def get_cookies():
    driver = webdriver.Firefox()
    driver.implicitly_wait(50)
    driver.get("https://dubai.dubizzle.com/")

    login_button = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/div/div[2]/button[3]')
    login_button.click()

    email_button = driver.find_element_by_xpath('//*[@id="popup_login_link"]')
    email_button.click()

    username = driver.find_element_by_xpath('//*[@id="popup_email"]')
    username.clear()
    username.send_keys('zahrajam1999@gmail.com')

    password = driver.find_element_by_xpath('//*[@id="popup_password"]')
    password.clear()
    password.send_keys('7learnzahra')

    login = driver.find_element_by_xpath('//*[@id="popup_login_btn"]')
    login.click()
    sleep(15)

    cookie = driver.get_cookies()

    driver.close()
    return cookie

get_cookies()


