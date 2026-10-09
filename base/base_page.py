from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # 将超时时间从10秒增加到30秒，适应云端服务器的慢速渲染
        self.wait = WebDriverWait(driver, 30)

    def find_element(self, locator):
        # 显式等待，直到元素可见
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        # 改为等待元素可点击，比等待存在更稳健
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text