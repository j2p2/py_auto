from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time
import unittest
from search_page import GoogleSearchPage

class GoogleSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def test_success(self):
        driver = self.driver
        search_page = GoogleSearchPage(driver)
        driver.get("http://www.google.com")
        assert "Google" in driver.title
        search_page.search_for("butts")
        assert "No results found." not in driver.page_source

    def test_failure(self):
        driver = self.driver
        driver.get("http://www.google.com")
        assert "Some other stuff" in driver.title
        search_page.search_for("butts")
        assert "No results found." not in driver.page_source
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()