import wikipediaapi
import requests
from selenium import webdriver

def wikipedia():

    wiki_wiki = wikipediaapi.Wikipedia('en')
    item = input("\n Enter the Topic : ")
    loc = 'C:\\Users\\dhemi\\PycharmProjects\\Cli-python\\package\\web_driver\\chromedriver.exe'

    page_py = wiki_wiki.page(item)
    print("Page - Exists: %s" % page_py.exists())
    # Page - Exists: True
    if(page_py.exists()==False):
        print("The page doesn`t exits :P")
    else:
        print("Page - Title: %s" % page_py.title)
        # Page - Title
        print("Page - Summary: %s" % page_py.summary[0:60])
        # Page - Summary
        input("press any key to open url")
        ur = page_py.fullurl
        driver = webdriver.Chrome(loc)
        driver.get(ur)
        print(ur)
        # https://en.wikipedia.org/wiki/Python_(programming_language)
        print(page_py.canonicalurl)
        # https://en.wikipedia.org/wiki/Python_(programming_language)
        #driver.close()

