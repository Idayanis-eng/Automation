import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Create a parent class that hold the information of the fixture and inherit it in this class (child class)
# @pytest.mark.usefixtures("setup")
from PageObject.CheckoutPage import CheckoutPage
from PageObject.ConfirmationPage import ConfirmationPage
from PageObject.HomePage import HomePage
from Utilties.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        # Create driver object that can connect the driver from homepage class
        homePage = HomePage(self.driver)
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # Since the click action was defined in the HomePage class under the method we do not need to performe it here
        # homePage.shopItems().click() # >> POM
        # And since the checkoutPage object was created on the HomePage under the method
        # We do not need to create the object here
        # Create driver object that can connect the driver from CheckoutPage class
        # checkoutPage = CheckoutPage(self.driver)
        checkoutPage = homePage.shopItems()
        # cards = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        cards = checkoutPage.getCardTitle()  # >> POM
        log.info("Getting all the cards titles")
        # i = -1
        for card in cards:
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                # card.find_element(By.XPATH, "div/button").click() #[i]
                card.checkoutPage.getCorrectCardText().click()

        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        # add item to cart
        checkoutPage.addItem().click()

        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        # go to check out page
        # Since the click action was defined in the CheckoutPage class under the method goToCheckOutPage()
        # we do not need to performe it here
        # checkoutPage.goToCheckOutPage().click()
        # We do not need to create the object here
        # Create driver object that can connect the driver from CheckoutPage class
        # Check out Page
        # Create driver object that can connect the driver from ConfirmationPage class
        # confirmationPage = ConfirmationPage(self.driver)
        confirmationPage = checkoutPage.goToCheckOutPage()

        # self.driver.find_element(By.ID, "country").send_keys("ind")
        # type ind in the search bar
        log.info("Entering country name")
        confirmationPage.enterText().send_keys("ind")


                 # time.sleep(5)
        # Explicit wait, method defined in Base Class
        self.verifyLinkPresence("India")

        # Click on the India
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmationPage.selectDropDownOption().click()

        # Click on Checkox
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmationPage.clickOnCheckBox().click()

        # Click on Submit
        #self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        confirmationPage.clickOnSubmit().click()

        #TextMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        textMatch = confirmationPage.verifyText().text
        log.info("Test recieved from applications is:"+textMatch)
        assert "Success! Thank you!" in textMatch

