class DemoAdminPage:
    def __init__(self,page):
        self.page = page
        self.admin_icon = page.locator("//a[@data-toggle='dropdown']")  # admin icon
        self.logout = page.locator("a[class='dropdown-item']").nth(1)  # logout option
        self.admin_more_info = page.locator('.small-box-footer').nth(1)



    def click_admin_icon(self):
        self.admin_icon.click()
        return self

    def click_logout(self):
        from Pages.demo_login_page import DemoLoginPage
        self.logout.click()
        return DemoLoginPage(self.page)

    def click_admin_more_info(self):
        from Pages.admin_list import AdminListPage
        self.admin_more_info.click()
        return AdminListPage(self.page)