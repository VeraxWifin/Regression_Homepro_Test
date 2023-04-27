import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import allure
from allure_commons.types import AttachmentType


@pytest.fixture()
def browser_chrome():
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.maximize_window()
    yield browser
    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    browser.quit()


@pytest.fixture()
def browser_firefox():
    services = FirefoxService(GeckoDriverManager().install())
    browser = webdriver.Firefox(service=services)
    browser.maximize_window()
    yield browser
    allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    browser.quit()