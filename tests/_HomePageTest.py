from pages.BaseClass import BaseObject
from pages.HomePage import HomePage
import unittest


class HomePage_Test(unittest.TestCase):
    def setUp(self):
        self.base = base = BaseObject(domain='https://www.slalom.com',driver='Firefox')
        self.base.setUp()
        self.browser = self.base.browser
        self.domain = self.base.domain
        self.Home = HomePage(self.browser, self.domain)

    def test_home_page_loads(self):
        self.Home.navigate_to_main_page()
        page_title = self.browser.title
        self.assertTrue(page_title == 'Home | Slalom','Home page title is incorrect')


    def tearDown(self):
        self.base.tearDown()