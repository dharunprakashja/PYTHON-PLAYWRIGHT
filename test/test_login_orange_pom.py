import re
from playwright.sync_api import Page
from pages.orange_page_home import HomePage
from pages.orange_page_login import LoginPage

def test_example(page:Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    home_page.is_upgrade_visible()
    home_page.click_dashbooard()