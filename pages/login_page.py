from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    # 元素定位（SauceDemo 网站的账号密码输入框和登录按钮）
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)