from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class InventoryPage(BasePage):
    FIRST_ITEM_ADD_BUTTON = (By.CSS_SELECTOR, ".inventory_item:first-child button")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_item_to_cart(self):
        """将第一个商品加入购物车"""
        self.click(self.FIRST_ITEM_ADD_BUTTON)
        # 点击后，强制等待购物车徽章在页面上渲染出来（最多等30秒）
        self.wait.until(EC.presence_of_element_located(self.SHOPPING_CART_BADGE))

    def get_cart_count(self):
        """获取购物车图标上的商品数量"""
        try:
            return self.get_text(self.SHOPPING_CART_BADGE)
        except Exception:
            return "0"

    def go_to_cart(self):
        """点击进入购物车页面"""
        self.click(self.SHOPPING_CART_LINK)