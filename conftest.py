# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Enter language')


@pytest.fixture(scope='function')
def browser(request):
    print('Start browser')
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    print('Quit browser')