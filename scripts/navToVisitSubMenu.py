
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

class navigateToGiftSubMenu():

    def test(self):
        baseUrl = "https://www.mga.edu"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(2)
        element = driver.find_element_by_xpath("//*[@id='primary-sub-menu']/li[4]/a")
        element.click()
        driver.implicitly_wait(2)

       
nav = navigateToGiftSubMenu()
nav.test() 