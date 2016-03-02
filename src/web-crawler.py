__author__ = 'gkannappan'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys
from bs4 import BeautifulSoup

import unittest, time, re

class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.ichangemycity.com/bangalore/complaints"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_sel(self):
        driver = self.driver
        delay = 1
        driver.get(self.base_url)
        #driver.get(self.base_url + "/search?q=stckoverflow&src=typd")
        driver.find_element_by_link_text("All").click()
        for i in range(1,10000):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        html_source = driver.page_source
        data = html_source.encode('utf-8')
        #data_bs = BeautifulSoup(data, 'html.parser')
        #print(data_bs.prettify())
        print(data)



if __name__ == "__main__":
    unittest.main()