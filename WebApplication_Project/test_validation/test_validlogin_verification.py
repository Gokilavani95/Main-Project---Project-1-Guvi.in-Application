from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from Page_locators import *
from Page_locators.Locators import home_locators

@pytest.mark.order(2)

class TestValidlogin:

    #Test Case-6:Verify login functionality with valid credentials
    def test_login_function(self,driver):
        login = home_locators(driver)
        login.open()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(login.login_button())).click()
        login.login_details("<valid username>","<valid password>")
        expected_url = "https://www.guvi.in/"
        WebDriverWait(driver, 20).until(EC.url_contains(expected_url))
        profile = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH,"//img[@alt='Profile'][1]")
            )
        )
        assert profile.is_displayed()
        print("Application logged in successfully")
