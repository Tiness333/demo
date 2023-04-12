import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLagou(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()


    def test_case001(self):
        self.driver.get("https://www.lagou.com")
        self.driver.set_window_size(1920,1080)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.ID, 'cboxClose')))
        self.driver.find_element(By.ID, "cboxClose").click()
        self.driver.find_element(By.ID,'search_input').click()
        self.driver.find_element(By.ID, 'search_input').send_keys('字节跳动')
        self.driver.find_element(By.ID,'search_button').click()
        time.sleep(1)
        slement=self.driver.find_element(By.CSS_SELECTOR,'.cl-right-top__1cCMk h3')
        assert '字节跳动' == slement.text

if __name__ == '__main__':
    unittest.main()
