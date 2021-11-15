from pages.BaseClass import BaseObject

class HomePage(BaseObject):
    def __init__(self, browser, domain):
        self.browser = browser
        self.domain = domain

    def navigate_to_main_page(self):
        self.browser.get(self.domain + '/home')

    def click_what_we_do(self):
        self.browser.find_element_by_link_text('what we do').click()