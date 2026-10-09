# Web UI 自动化测试框架

## 📖 项目简介
基于 Python + Selenium + Pytest 搭建的 Web UI 自动化测试框架，采用 POM（页面对象模型）设计模式，针对 Saucedemo 电商网站的核心业务流（登录、加购）进行端到端自动化测试。

## 🛠️ 技术栈
- 测试框架：Python、Pytest、Selenium
- 设计模式：POM (Page Object Model)
- 持续集成：GitHub Actions
- 浏览器：Chrome Headless (无头模式)

## 📂 项目结构
- `base/`：基类，封装 Selenium 通用方法（等待、点击、输入）
- `pages/`：页面对象层（登录页、商品页的元素定位与操作）
- `testcases/`：测试用例层（登录流程、加购流程）
- `conftest.py`：全局 Driver 管理

## 🚀 如何运行
1. 安装依赖：`pip install -r requirements.txt`
2. 执行测试：`pytest testcases/ -s`

## 💡 项目亮点
- POM 设计模式：代码分层清晰，元素定位与测试逻辑分离，可维护性强
- 无头模式运行：集成 CI 环境，无需 GUI 即可执行测试
- 业务流覆盖：覆盖登录成功、异常登录拦截、加入购物车并断言购物车数量等核心场景