from playwright.sync_api import Page,expect

class HomePage:

    def __init__(self, page:Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button",name="Upgrade")
        self.dashboard_link = page.get_by_role("link",name="Dashboard")

    def is_upgrade_visible(self):
        expect(self.upgrade_button).to_be_visible()

    def click_dashbooard(self):
        self.dashboard_link.click