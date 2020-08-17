from selenium import webdriver
import time 

def amz_pr( prod ):
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")

    
    searchBox = driver.find_element_by_id("twotabsearchtextbox")
    searchBox.send_keys(prod)
    searchBox.send_keys(u'\ue007')
    time.sleep(5)

    product = driver.find_element_by_class_name('a-badge')
    product.click()

    global price
    price = driver.find_element_by_id("priceblock_ourprice").text

    time.sleep(5)

    driver.quit()
    print("The Price of ", prod, 'on Amazon is:', price)
    