import pytest
from selene import browser


@pytest.fixture(autouse=True )
def browser_management():
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 800
    browser.config.window_width = 1200
    yield
    browser.quit()

