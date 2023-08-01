import time

from selenium import webdriver
from selenium.webdriver.common.by import By
class Test_orangedemo_001:
    def test_loginOrangeHRM_001(self):
        driver=webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        #Enter username
        driver.find_element(By.NAME,'username').send_keys('Admin')
        #Enter password
        driver.find_element(By.NAME, 'password').send_keys('admin123')
        #Click on login button
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        if driver.title == 'OrangeHRM':
            print("Login success to OrangeHRM site")
            assert True
        else:
            print("Not reachable to orangeHRM site")
            driver.close()
            assert False