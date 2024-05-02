import pytest
from selene import browser, have


@pytest.fixture(scope='module')
def browser_management():
   browser.config.driver_name = 'chrome'
   browser.config.base_url = 'https://google.com'
   browser.config.window_height = 500
   browser.config.window_width = 1200

