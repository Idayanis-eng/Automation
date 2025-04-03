from selenium.webdriver.common.by import By


class ConfirmationPage:

    def __init__(self, driver):
        self.driver = driver

    searchBar = (By.ID, "country")
    dropDownText = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    sumitButt = (By.CSS_SELECTOR, "[type='submit']")
    successText = (By.CSS_SELECTOR, "[class*='alert-success']")

    def enterText(self):
        return self.driver.find_element(*ConfirmationPage.searchBar)

    def selectDropDownOption(self):
        return self.driver.find_element(*ConfirmationPage.dropDownText)

    def clickOnCheckBox(self):
        return self.driver.find_element(*ConfirmationPage.checkBox)

    def clickOnSubmit(self):
        return self.driver.find_element(*ConfirmationPage.sumitButt)

    def verifyText(self):
        return self.driver.find_element(*ConfirmationPage.successText)

