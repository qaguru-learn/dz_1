from selene import browser, be, have


browser.open('https://www.ecosia.org')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="main"]').should(have.text('User-oriented Web UI browser tests in Python. Contribute to yashaka/selene development by creating an account on GitHub.'))
