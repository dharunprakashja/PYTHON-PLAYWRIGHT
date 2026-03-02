import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").press("CapsLock")
    page.get_by_role("textbox", name="Username").fill("ADD")
    page.get_by_role("textbox", name="Username").press("CapsLock")
    page.get_by_role("textbox", name="Username").press("CapsLock")
    page.get_by_role("textbox", name="Username").fill("ADMIN")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("ADMIN1")
    page.get_by_role("textbox", name="Password").press("CapsLock")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("textbox", name="Password").press("Enter")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("canvas").first).to_be_visible()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
