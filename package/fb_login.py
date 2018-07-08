from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

loc = 'C:\\Users\\dhemi\\PycharmProjects\\Cli-python\\package\\web_driver\\chromedriver.exe'

def login():
    print("\t Enter the facebook credential`s \n")
    mail = input("\t Enter Email :")
    passw = getpass.getpass()
    driver = webdriver.Chrome(loc)
    driver.get('https://www.facebook.com/')
    email = driver.find_element_by_name('email')
    email.clear()
    email.send_keys(mail)
    password = driver.find_element_by_name('pass')
    password.send_keys(passw)
    button = driver.find_elements_by_id('loginbutton')
    password.send_keys(Keys.RETURN)
    while True :
        ch = input("press q to close window \n ")
        if (ch=='q'):
            driver.close()
            break




