from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import apikeys


def openLinkedIn(postContent):
    profile = webdriver.FirefoxProfile('add your firefox profile')
    driver = webdriver.Firefox(firefox_profile=profile)

    driver.get('https://www.linkedin.com')
    time.sleep(5)
    # Find an element on the page and interact with it
    searchBox = driver.find_element(By.CLASS_NAME,'share-box-feed-entry__closed-share-box')	
    searchBox2 = searchBox.find_element(By.CLASS_NAME,'artdeco-button')
    searchBox2.click()
    time.sleep(5)
    pyautogui.click(-2066,558)
    pyautogui.write(postContent)


  
    # Close the browser window
    #driver.quit()
