
from selenium import webdriver
from selenium.webdriver.common.by import By
from homepage import locate
import time
from webdriver_manager.chrome import ChromeDriverManager

class navigateToKnightAlert():

    def test(self):
        baseUrl = "https://www.mga.edu"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(2)
        element = driver.find_element_by_xpath(locate('knight alert'))
        element.click()
        driver.implicitly_wait(2)

       
nav = navigateToKnightAlert()
nav.test()