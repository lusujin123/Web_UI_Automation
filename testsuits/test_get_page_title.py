# coding=utf-8
import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUp(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_get_title(self):

        homepage = HomePage(self.driver)
        print(homepage.get_page_title())

