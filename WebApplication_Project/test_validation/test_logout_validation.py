from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Page_locators.Locators import home_locators
import pytest

@pytest.mark.order(6)
class Test_logout():
    # Test Case-10: Validate logout functionality.
    def test_logout(self,driver):
        logout_obj = home_locators(driver)
        logout_obj.open()
        logout_obj.login_button().click()
        logout_obj.login_details("<valid username>","<valid password>")

        profile = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located(
                (By.XPATH,"//img[@alt='Profile'][1]")
            )
        )

        assert profile.is_displayed()
        profile.click()
        signout_icon = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located
                (logout_obj.signout())

        )
        signout_icon.click()
        print("Web page logged out successfully")


