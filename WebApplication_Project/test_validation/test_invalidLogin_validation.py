from Page_locators.Locators import *
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

@pytest.mark.order(3)
class TestInvalidLogin:
    #Test case- 7: Verify login with invalid credentials.
    #Below methods are different invalid combination validations
    def test_balnk_username_password(self,driver):
        invalid_login = home_locators(driver)
        #launch the url
        invalid_login.open()

        #Click to navigate Loginpage
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(invalid_login.login_button())
        ).click()

        #pass blank username and password
        invalid_login.login_details("","")
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,"//div[text()='Hey, Did you forgot your password? Try again.']"))
        )
        assert error.is_displayed()
        print("Blank username and Password")

    def test_blankpassword(self,driver):
        blank_password = home_locators(driver)
        blank_password.open()

        blank_password.login_button().click()
        blank_password.login_details("<valid username>","")
        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH,"//div[text()='Hey, Did you forgot your password? Try again.']")
            )
        )

        assert error.is_displayed()
        print("Blank password. Enter valid password and try again")

    def test_invalidlogin(self,driver):
        invalid_login = home_locators(driver)
        invalid_login.open()

        invalid_login.login_button().click()
        invalid_login.login_details("gokila12@gmail.com","123")

        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH,"//div[text()='Incorrect Email or Password']")
            )
        )

        assert error.is_displayed()
        print("Incorrect Email or Password. Try with valid username and password")








