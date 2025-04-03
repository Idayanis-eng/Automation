import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        # Need to create an object to be able to log
        # inspect.stack() returns a list with frame records.
        # In function whoami(): inspect.stack()[1] is the frame record of the function that calls whoami, like foo() and bar().
        # The fourth element of the frame record (inspect.stack()[1][3]) is the function name.
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)

        # Crete an object (file) that will print all the information present in the logger object
        fileHandler = logging.FileHandler('logfile.log')

        # Formatting the file
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        # Pass the format information to the logger object through fileHandler
        fileHandler.setFormatter(formatter)

        # Pass the fileHandler object to logger object
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)

        return logger

    # Costume utilities
    # Verify link presence  by explicitly wait
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    # Select dropdown
    def selectDropDown(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)


