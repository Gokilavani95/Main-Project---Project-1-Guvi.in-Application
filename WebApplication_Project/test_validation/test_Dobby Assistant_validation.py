from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Page_locators.Locators import home_locators

@pytest.mark.order(5)
class TestDobbyAssistant():
    #Test case-9:Validate that the Dobby Guvi Assistant is present on the page
    def test_chatbox_validation(self,driver):
        chat = home_locators(driver)
        chat.open()
        chat.login_button().click()
        chat.login_details("<valid username>","<valid password")
        WebDriverWait(driver,10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt='Profile'][1]")
            )
        )

        message_box = WebDriverWait(driver,30).until(
            EC.visibility_of_element_located(
                chat.chatbox()
            )
        )
        #message_box = chat.chatbox()
        assert message_box.is_displayed() and message_box.is_enabled()
        print("Chat box is accessible")
