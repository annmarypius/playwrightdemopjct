class DemoLoginPage:
    def __init__(self,page):
        self.page=page

        self.username=page.get_by_placeholder("Username")
        self.password=page.get_by_placeholder("Password")
        #self.sign_in=page.locator("//button[text()='Sign In']")
        self.sign_in = page.locator("//button[@class='btn btn-dark btn-block']")


    def enter_username(self,user):
        self.username.fill(user)
        return self


    def enter_password(self,pwd):
        self.password.fill(pwd)
        return self

    def click_sign_in(self):
        from Pages.admin_page import DemoAdminPage
        self.sign_in.click()
        #return DemoLoginPage(self.page)
        return DemoAdminPage(self.page)
    #The process is called as circular import
    #incase of test cases chaining method can be implemented between methods as
    #well as POM pages



