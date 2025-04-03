from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PageObject.CheckoutPage import CheckoutPage


class HomePage:
    # create a contractor for the driver object that can connect to our test case (class test)
    def __init__(self, driver):
        self.driver = driver

    # Here we will declare object for all the elements we need to test in the home page
    # In our case we are clicking on the shop button on top of the page

    # Declare a variable shop for the objcet
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    nameField = (By.CSS_SELECTOR, "input[name='name']")
    emailField = (By.NAME, "email")
    passwordField = (By.ID, "exampleInputPassword1")
    checkBox = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    radioButton = (By.CSS_SELECTOR, "#inlineRadio1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    messageText = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # The * will deserialize the tupple and get all the elements inside it
        # Optimizing the code. By adding .click() and right after creating the object to handle the next page and returning the object
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.nameField)

    def getEmailAdress(self):
        return self.driver.find_element(*HomePage.emailField)

    def getPassword(self):
        return self.driver.find_element(*HomePage.passwordField)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox).click()

    def getDropDown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getRadioButton(self):
        return self.driver.find_element(*HomePage.radioButton).click()

    def submitForm(self):
        return self.driver.find_element(*HomePage.submitButton).click()

    def getMessage(self):
        return self.driver.find_element(*HomePage.messageText).text

