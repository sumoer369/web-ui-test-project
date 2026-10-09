import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    # 配置 Chrome 无头模式（后台运行，不弹窗，CI/CD 必备）
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()


def test_successful_login(driver):
    """测试正常登录"""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # 断言：登录成功后 URL 会变成 /inventory.html
    assert "inventory" in driver.current_url
    print("成功登录测试通过！")


def test_locked_out_user(driver):
    """测试被锁定用户登录失败"""
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    # 断言：页面会出现错误提示
    error_message = login_page.get_text((By.CSS_SELECTOR, "[data-test='error']"))
    assert "Sorry, this user has been locked out" in error_message
    print("锁定用户拦截测试通过！")