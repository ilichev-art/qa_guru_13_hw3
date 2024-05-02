from selene import browser, be, have


def test_find_element(browser_management):
   browser.open('/')
   browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
   browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_no_find_element(browser_management):
   browser.open('/')
   browser.element('[name="q"]').should(be.blank).type('-тест').press_enter()
   browser.element('//*[@id="slim_appbar"]/div').should(have.text('Результатов: примерно 0'))

