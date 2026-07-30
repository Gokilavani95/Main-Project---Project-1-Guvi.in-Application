from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_locators.Locators import home_locators
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.order(4)
class Test_Homepage:
    #Test Case-8: Verify that menu items like “Courses”, “LIVE Classes”, and “Practice” are displayed.
    def test_homepage(self,driver):
        home_page = home_locators(driver)
        home_page.open()

        home_page.login_button().click()

        home_page.login_details("<valid username>","<valid password>")
        profile = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//img[@alt='Profile'][1]")
            )
        )
        assert profile.is_displayed()

        live_class = home_page.home_Liveclass()
        assert live_class.is_displayed()
        assert live_class.is_enabled()
        print("Live class option is displayed")

        #To validate Live Class subsection on action
        # actions = ActionChains(driver)
        # actions.move_to_element(live_class).perform()
        # menu = WebDriverWait(driver, 20).until(
        #     EC.visibility_of_element_located(
        #         (By.XPATH,"/html[1]/body[1]/main[1]/header[1]/div[1]/div[3]/div[1]/div[2]/div[2]")
        #     )
        # )
        # menu.is_displayed()
        # print("Live class sub menu is displayed")

        course = home_page.courses()
        assert course.is_displayed() and course.is_enabled()
        print("Course option is accessible")

        practice = home_page.practice()
        assert practice.is_displayed() and practice.is_enabled()
        print("Practice option is accessible")

        resource = home_page.Resources()
        assert resource.is_displayed() and resource.is_enabled()
        print("Resource option is accessible")

        product=home_page.Our_Products()
        assert product.is_displayed() and product.is_enabled()
        print("Product option is accessible")


