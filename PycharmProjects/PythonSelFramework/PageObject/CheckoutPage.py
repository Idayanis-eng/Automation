from selenium.webdriver.common.by import By

from PageObject.ConfirmationPage import ConfirmationPage


class CheckoutPage:
    # Declare a constructor for driver to connect to test class
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardText = (By.XPATH, "div/h4/a")
    correctCardText = (By.XPATH, "div/button")
    addItemButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutButton = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitle(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardText(self):
        return self.driver.find_element(*CheckoutPage.cardText)

    def getCorrectCardText(self):
        return self.driver.find_element(*CheckoutPage.correctCardText)

    def addItem(self):
        return self.driver.find_element(*CheckoutPage.addItemButton)

    def goToCheckOutPage(self):
        self.driver.find_element(*CheckoutPage.checkOutButton).click()
        confirmationPage = ConfirmationPage(self.driver)
        return confirmationPage
