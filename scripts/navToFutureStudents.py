from selenium import webdriver
from homepage import locate
from webdriver_manager.chrome import ChromeDriverManager

class navigateToFutureStudents():

    def test(self):
        baseUrl = "https://www.mga.edu"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        driver.implicitly_wait(2)
        element = driver.find_element_by_xpath(locate('future students'))
        element.click()
        driver.implicitly_wait(2)

       
nav = navigateToFutureStudents()
nav.test()