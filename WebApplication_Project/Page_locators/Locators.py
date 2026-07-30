import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import page_url


class home_locators:


    def __init__(self,driver):
        self.driver=driver
        self.username_field = (By.ID,"email")
        self.password_field = (By.ID,"password")
        self.login_btn = (By.XPATH,"//a[@class='btn login-btn']")



    def open(self):
        self.driver.get(page_url)

    def login_button(self):
        return self.driver.find_element(By.XPATH, "(//button[@id='login-btn'])[1]")

    def sign_up_button(self):
        return self.driver.find_element(By.XPATH,"(//button[text()='Sign up'][1])")

    def sign_up_page(self):
        return self.driver.find_element(By.XPATH,"//p[normalize-space()='Or Sign Up with Email']")

    def login_details(self,username,password):
        username_web = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_field)
        )
        username_web.clear()
        username_web.send_keys(username)

        password_web = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_field)
        )
        password_web.clear()
        password_web.send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    def home_Liveclass(self):
        return self.driver.find_element(By.XPATH, "//p[text()='LIVE Classes']")

    def courses(self):
        return self.driver.find_element(By.XPATH, "//p[text()='Courses']")

    def practice(self):
        return self.driver.find_element(By.XPATH, "//p[text()='Practice']")

    def Resources(self):
        return self.driver.find_element(By.XPATH, "//p[text()='Resources']")

    def Our_Products(self):
        return self.driver.find_element(By.XPATH, "//p[text()='Our Products']")

    def chatbox(self):
        return (By.ID,"zs_fl_chat")

    def signout(self):
        return (By.XPATH,"//p[text()='Sign Out'][1]")

