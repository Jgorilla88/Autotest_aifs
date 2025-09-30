import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome


@pytest.fixture
def driver():
    opt = Options()
    opt.add_argument('--headless')
    opt.add_argument('--window-size=1920,1080')

    browser = Chrome(options=opt)
    yield browser
    browser.quit()
