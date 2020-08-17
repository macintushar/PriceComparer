from selenium import webdriver
import time 

def flip_prod( prod ):

    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    loginClose = driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
    loginClose.click()

    time.sleep(5)

    searchBox = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
    searchBox.send_keys(prod)
    searchBox.send_keys(u'\ue007')

    time.sleep(5)
    global price
    price = driver.find_element_by_class_name("_6BWGkk").text

    time.sleep(5)
    driver.quit()
    print("The Price of ", prod, 'on Flipkart is:', price)
 