from selene import browser, be, have

browser.open('https://duckduckgo.com')
browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
#browser.element('[title="Нет, спасибо"]').click()
browser.element('html').should(have.text('Курсы Тестировщиков'))