from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import os
import datetime

class BaseObject():

    def __init__(self, domain=None, driver='Firefox'):
        self.driver = 'Firefox'
        self.domain = domain
        self.delay = 30
        self.implicit_wait = 5
        self.options = None
        self.browser = None

    def firefox_configuration(self):
        self.options = FirefoxOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--incognito')
        self.browser = webdriver.Firefox(
            executable_path = os.path.join(os.getcwd(), '../drivers', 'Windowsgeckodriver.exe'),
            options=self.options
        )

    def setUp(self):
        if self.driver=='Firefox':
            self.firefox_configuration()
        self.browser.set_page_load_timeout(self.delay)
        self.browser.implicitly_wait(self.implicit_wait)
        self.browser.fullscreen_window()

    def tearDown(self):
        self.browser.close()

    def CapturesScreenshot(self, fileStartName):
        self.browser.save_screenshot(os.path.join('../error_screenshots', (fileStartName + "_" + datetime.utcnow().strftime("%Y%m%d%H%M%S") + ".png")))