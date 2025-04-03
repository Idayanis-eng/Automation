
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Declare command line argument. Add a command line option and provide a cmdopt(command option) through a fixture func
# So that through command line we can select in which browser we want out test to run
# The code can be copied from the oficial website docs.pytest.org - command line option pytest
# We can tell this is a hook for adding a command line option
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    # Retrieve command line value declared before
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("/Users/idasaravanan/Desktop/tools/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        # driver = webdriver.Chrome(executable_path="/Users/idasaravanan/Desktop/tools/chromedriver")
    elif browser_name == "firefox":
        obj_service = Service("/Users/idasaravanan/Desktop/tools/geckodriver")
        driver = webdriver.Firefox(service=obj_service)
        # driver = webdriver.Firefox(executable_path="/Users/idasaravanan/Desktop/tools/geckodriver")
    elif browser_name == "IE":
        print("Run on IE")
    driver.implicitly_wait(4)
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.close()

