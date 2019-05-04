
from selenium import webdriver
from selenium.webdriver.common.by import By
from homepage import locate
import time
from webdriver_manager.chrome import ChromeDriverManager

class navigateToStudentAffairs():

    def test(self):
        baseUrl = "https://www.mga.edu"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(2)
        element = driver.find_element_by_xpath(locate('student affairs'))
        element.click()
        driver.implicitly_wait(2)

       
nav = navigateToStudentAffairs()
nav.test()