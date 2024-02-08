from selene import browser, be, have


browser.open('https://ya.ru')
browser.element('[id="text"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search-result"]').should(have.text('Contribute to yashaka/selene development by creating an account on GitHub'))
