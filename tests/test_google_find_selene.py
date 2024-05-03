from selene import browser, be, have


def test_find_element():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_no_find_element():
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('-тест').press_enter()
    browser.element('.LHJvCe').should(have.text('Результатов: примерно 0'))



