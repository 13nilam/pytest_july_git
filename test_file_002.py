from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_CredenceLogin_002:
    #@pytest.mark.skip
    def test_logintoCredence(self):

        # 1)open browser
        driver = webdriver.Chrome()
        # 2)Open URL
        driver.get("https://automation.credence.in/login")
        # 3)Enter E-Mail Address
        driver.find_element(By.CSS_SELECTOR, "input[id='email']").send_keys('Credencetest@test3.com')
        # 4)Enter Password
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys('Credence@123')
        # 5)Clik on login button
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            print("Login TestCase is Passed")
            assert True
        except:
            print("Login TestCase is Failed")
            driver.close()
            assert False
        driver.close()
    def test_sub_002(self):
        a = 10
        b = 20
        sub = a - b
        print("Mul=a+b", sub)
        if sub == -10:
            print("sub matched")
            assert True
        else:
            print("sub not matched")
            assert False

