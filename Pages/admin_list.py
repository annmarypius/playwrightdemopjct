class AdminListPage:
    def __init__(self,page):
        self.page=page
        self.new_button=page.locator("a[class='btn btn-rounded btn-danger']")
        self.new_user=page.locator("#username")
        self.new_password = page.locator("#password")
        self.usertype_field = page.locator("//select[@name='user_type']")
        self.create_button=page.locator("//button[@name='Create']")
        self.popup_field_failure = page.locator("//div[contains(@class,'alert-danger')]")
        self.popup_field_success = page.locator("//div[contains(@class,'alert-success')]")
        self.search_button=page.locator("//a[@class='btn btn-rounded btn-primary']")
        self.username=page.locator("#un")
        self.user_type=page.locator("#ut")
        self.search_user=page.locator("//button[@name='Search']")
        self.table = page.locator("//table[@class='table table-bordered table-hover table-sm']/tbody/tr[1]/td[1]")
        #self.table=page.locator(".table table-bordered table-hover table-sm")
        #self.username_value=table.locator("tbody/tr[1]/td[1]").text_content()


    def click_new_button(self):
        self.new_button.click()
        return self

    def fill_new_user(self,new_user1):
        self.new_user.fill(new_user1)
        return self

    def fill_new_password(self,newpwd1):
        self.new_password.fill(newpwd1)
        return self

    def add_new_usertype(self):
        self.usertype_field.select_option("staff")
        return self

    def click_save_button(self):
        self.create_button.click()
        return self

        # this method is for username already exists case [based on alert-danger]

    
        return self.popup_field_failure.text_content()

        # this method is for user created successfulyy case [based on alert-success]
    def isPopupVisible_new_user(self):
        print( self.popup_field_success.text_content())

    def click_search(self):
        self.search_button.click()

    def enter_username(self,username):
        self.username.fill(username)

    def select_usertype(self):
        self.user_type.select_option("staff")

    def click_search_user(self):
        self.search_user.click()

    def table_result(self):
        res = self.table.text_content()
        print(f'The username available in table is: {res}')

    def table_result(self):
        res = self.table.text_content()
        print(f'The username available in table is: {res}')
        return self.table



