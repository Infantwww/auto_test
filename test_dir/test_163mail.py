from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from parameterized import parameterized


class Test_mail_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.mail_url = 'https://mail.163.com'

    def mail_163(self, sendkey1, sendkey2):
        self.driver.get(self.mail_url)
        time.sleep(2)
        login_frame = self.driver.find_element(By.CSS_SELECTOR, '[id^=x-URS-iframe]')
        self.driver.switch_to.frame(login_frame)
        self.driver.find_element(By.CSS_SELECTOR, '[name = email]').clear()
        self.driver.find_element(By.CSS_SELECTOR, '[name = email]').send_keys(sendkey1)
        self.driver.find_element(By.CSS_SELECTOR, '[name = password]').clear()
        self.driver.find_element(By.CSS_SELECTOR, '[name = password]').send_keys(sendkey2)
        self.driver.find_element(By.CSS_SELECTOR, '#dologin').click()
        time.sleep(2)

    @parameterized.expand([
        ('15216678682', 'wang8023?'),
    ])
    def test_login(self, sendkey1, sendkey2):
        self.mail_163(sendkey1, sendkey2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Test_mail_login('test_login'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
