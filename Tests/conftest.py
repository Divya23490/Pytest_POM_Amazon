import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Config.config import TestData

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param=="chrome":
        s = Service(ChromeDriverManager().install())
        web_driver=webdriver.Chrome(service=s)
    request.cls.driver=web_driver
    yield
    web_driver.close()

