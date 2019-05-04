import navToPolice, navtoapply, navtoaboutmga, navToAddressMap, navToAdmissions, navToAlumni, navtoCurrentStudents,navToCustomerService, navToEmployment, navToFacebook
from selenium import webdriver
class homepageWrapperFunction():
    def navigateHomePage(self):
        navigatetopolice()
        navigatetoapply()
        navigatetoaboutmga()
        navigatetoaddressmap()
        navigatetoadmissions()
        navigateToAlumni()
        navigatetocurrentstudents()
        navigateToCustomerService()
        navigatetoemployment()
        navigatetofacebook()

test=homepageWrapperFunction
test.navigateHomePage()
