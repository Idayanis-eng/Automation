import pytest
from selenium import webdriver

# Chrome Driver
from selenium.webdriver.chrome.service import Service
# Path where the chromedriver is located
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilties.BaseClass import BaseClass


class TestHomePage(BaseClass):

    # Test Case (method)
    def test_formSubmition(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info(" The Name is: " + getData["name"])
        homepage.getName().send_keys(getData["name"])
        homepage.getEmailAdress().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheckBox()
        # Reusable function is present in the base class in the utilities package
        self.selectDropDown(homepage.getDropDown(), getData["gender"])

        homepage.getRadioButton()
        homepage.submitForm()
        homepage.getMessage()
        # Inspect element to find the locators
        #driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        #driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
        #driver.find_element(By.ID, "exampleCheck1").click()

        # To create syntax for CSSSelector -> tagneme[@atribute='value'] ->input[name='name]
        #driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")

        # Plugging to validate the locator for Chrome -> Selectorhub
        # check radio botton find element by CSS
        # CSS - tagname[attribute='value'] -> //input[@type='submit']
        # #id,
        # .classname
        #driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

        # Static Dropdown
        # dropdown.select_by_value() -> when value is defined in the you can use this method
        #dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # Select by index, starts with [0,1,2,3]
        #dropdown.select_by_index(0)
        # Select by visible text -> enter the text that are apearing in the dropdown
        #dropdown.select_by_visible_text("Female")

        # To create syntax for xpath -> //tagname[@atribute='value'] -> //input[@type='submit']
        # to click on the submit button
        #driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # after submit the form we will like to verify the message that is prompting on the page.
        #message = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(homepage.getMessage())

        # Check if the String is present in the message
        assert 'Success' in homepage.getMessage()

        #driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hallo")
        # to clear the textbox
        #driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

        # refresh the browser to load the other set of data
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param





