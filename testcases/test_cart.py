from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_to_cart(driver):
    """测试登录后，将商品加入购物车，验证购物车数量正确"""
    # 1. 登录
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # 2. 在商品页进行购物车操作
    inventory_page = InventoryPage(driver)

    # 断言：初始状态下，购物车没有数字徽标
    assert inventory_page.get_cart_count() == "0"

    # 操作：添加第一个商品
    inventory_page.add_first_item_to_cart()

    # 断言：购物车数量应该变成 1
    assert inventory_page.get_cart_count() == "1"

    # 3. 进入购物车页面
    inventory_page.go_to_cart()

    # 断言：页面跳转成功，URL 包含 cart
    assert "cart" in driver.current_url
    print("加入购物车流程测试通过！")