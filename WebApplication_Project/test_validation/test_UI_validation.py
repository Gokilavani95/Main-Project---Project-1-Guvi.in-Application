
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from Page_locators.Locators import home_locators

@pytest.mark.order(1)
class TestLogin:
    #Test Case:1
    def test_launch_url(self,driver):
        url = home_locators(driver)
        url.open()
        expected_url = "https://www.guvi.in"
        actual_url = driver.current_url.rstrip("/")
        assert expected_url == actual_url
        print("Test Passed, Application launched without any error")

    #Test Case:2
    def test_login(self,driver):
        obj = home_locators(driver)
        obj.open()
        expected_title = "HCL GUVI | Learn to code in your native language"
        actual_title = driver.title
        assert expected_title == actual_title
        print("Test passed",expected_title, " is equal to ",actual_title)


    #Test Case:3
    def test_login_button_validation(self,driver):
        btn = home_locators(driver)
        login_btn = btn.login_button()
        assert login_btn.is_displayed()
        print("Login button is displayed")
        assert login_btn.is_enabled()
        print("Login button is enabled")
        login_btn.click()
        email_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,"//input[@id='email']"))
        )
        assert email_field.is_displayed()
        print("Login page is opened successfully")


    #Test case:4 Verify visibility and clickability of the Sign-Up button.
    def test_signup(self,driver):
        sign_btn_obj = home_locators(driver)
        sign_btn_obj.sign_up_button().is_displayed()
        print("Signup button is displayed")
        assert sign_btn_obj.sign_up_button().is_enabled()
        print("Signup button is enabled")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                sign_btn_obj.sign_up_button()
            )
        )
        sign_btn_obj.sign_up_button().click()
        WebDriverWait(driver, 20).until(
            EC.url_matches
            ("https://www.guvi.in/register/")
        )
        print("Signup page is opened successfully")

    #Test-Case-5 : Verify navigation to the Sign-In page via the Sign-Up button.
    def test_signup_navigation(self,driver):
        sgn_up = home_locators(driver)
        button = sgn_up.sign_up_button()
        button.is_enabled()
        button.is_displayed()
        button.click()
        expected_url = "https://www.guvi.in/register/"
        WebDriverWait(driver, 20).until(EC.url_contains("https://www.guvi.in/register/"))
        assert driver.current_url.startswith(expected_url)
        sgn_up.sign_up_page().is_displayed()
        print("Sign up page is launched successfully")


