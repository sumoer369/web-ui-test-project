from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def test_successful_login(driver):
    """测试正常登录"""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url
    print("成功登录测试通过！")


def test_locked_out_user(driver):
    """测试被锁定用户登录失败"""
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    error_message = login_page.get_text((By.CSS_SELECTOR, "[data-test='error']"))
    assert "Sorry, this user has been locked out" in error_message
    print("锁定用户拦截测试通过！")