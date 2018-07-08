from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import pickle

loc = 'C:\\Users\\dhemi\\PycharmProjects\\Cli-python\\package\\web_driver\\chromedriver.exe'

def do_insta():
    print("\t Enter the instagram credential`s \n")
    mail = input("\t Enter Email :")
    passw = getpass.getpass("\t Password:")
    driver = webdriver.Chrome(loc)
    driver.get('https://www.instagram.com/accounts/login/?hl=en')
    email = driver.find_element_by_name("username")
    email.clear()
    email.send_keys(mail)
    password = driver.find_element_by_name('password')
    password.send_keys(passw)
    button = driver.find_elements_by_id('loginbutton')
    password.send_keys(Keys.RETURN)
    driver.get('https://www.instagram.com/dhemiwalnitin/following/?hl=en')
    unfollow = driver.find_elements_by_id("NroHT")

    while True :
        ch = getpass.getpass("press q to close window \n")
        if (ch=='q'):
            driver.close()
            break






