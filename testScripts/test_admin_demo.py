from playwright.sync_api import Page,expect
from constants.constant import login_url
from utilities.excel_read import NewExcelReader
from Pages.saucedemo_login_page import PomLoginPage
from Pages.demo_login_page import DemoLoginPage
import pytest

from Pages.admin_page import DemoAdminPage
from Pages.admin_list import AdminListPage


class TestAdminRights:
    def test_admin_Add_user(self,page: Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.get_by_text("Sign In").click()
        page.locator(".small-box-footer").nth(1).click()#more info
        page.locator(".btn btn-rounded btn-danger").click()#new button
        page.locator("#username").fill("ann123")
        page.locator("#password").fill("ann123")
        page.select_option("#user_type",label='Staff')
        #

        page.locator(".card.card-dark").nth(0).screenshot(path="screenshots/image3.png")
        page.locator(".card.card-dark").nth(1).screenshot(path="screenshots/image3.png")
        page.locator("button[name='Create']").click()
        alert=page.locator(".alert alert-success alert-dismissible")
        expect(alert).to_be_visible()

    def test_admin_Add_Existing_user(self,page: Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.get_by_text("Sign In").click()
        page.locator(".small-box-footer").nth(1).click()#more info
        page.locator(".btn btn-rounded btn-danger").click()#new button
        page.locator("#username").fill("ann123")
        page.locator("#password").fill("ann123")
        page.select_option("#user_type",label='Staff')
        page.locator("button[name='Create']").click()
        alert=page.locator(".alert alert-danger alert-dismissible")
        expect(alert).to_contain_text("Username already exists")

##############################################################################
    #using POM
    def test_admin_dashboard_pom(self,page:Page):
        page.goto(login_url)
        demo = DemoLoginPage(page)
        demo.enter_username("admin")
        demo.enter_password("admin")
        demo.click_sign_in()
        admin=DemoAdminPage(page)
        admin.click_admin_more_info()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin/list-admin")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_admin_dashboard_logout_pom(self,page:Page):
        page.goto(login_url)
        demo = DemoLoginPage(page)
        demo.enter_username("admin")
        demo.enter_password("admin")
        demo.click_sign_in()
        admin=DemoAdminPage(page)
        admin.click_admin_icon()
        admin.click_logout()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin/login")
    @pytest.mark.smoke
    def test_create_new_user_pom(self,page: Page):
        page.goto(login_url)
        demo = DemoLoginPage(page)
        demo.enter_username("admin")
        demo.enter_password("admin")
        demo.click_sign_in()
        admin = DemoAdminPage(page)
        admin.click_admin_more_info()
        new = AdminListPage(page)
        new.click_new_button()
        new.fill_new_user("John123")
        new.fill_new_password("John123")
        new.add_new_usertype()
        new.click_save_button()
        new.isPopupVisible_new_user()

    def test_create_existing_user_pom(self, page: Page):
        page.goto(login_url)
        demo = DemoLoginPage(page)
        demo.enter_username("admin")
        demo.enter_password("admin")
        demo.click_sign_in()
        admin = DemoAdminPage(page)
        admin.click_admin_more_info()
        new = AdminListPage(page)
        new.click_new_button()
        new.fill_new_user("John123")
        new.fill_new_password("John123")
        new.add_new_usertype()
        new.click_save_button()
        new.isPopupVisible()

    def test_search_username(self,page: Page):
        page.goto(login_url)
        demo = DemoLoginPage(page)
        demo.enter_username("admin")
        demo.enter_password("admin")
        demo.click_sign_in()
        admin = DemoAdminPage(page)
        admin.click_admin_more_info()
        new = AdminListPage(page)
        new.click_search()
        new.enter_username("ann123")
        new.select_usertype()
        new.click_search_user()
        new.table_result()

    #POM chaining for admin user addition
    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.endtoend
    def test_admin_Add_user_with_pomchaining(self,page: Page):
        page.goto(login_url)
        demo = DemoLoginPage(page)
        demo.enter_username("admin").enter_password("admin").click_sign_in().click_admin_more_info().click_new_button().fill_new_user("james123").fill_new_password("james123").add_new_usertype().click_save_button().isPopupVisible_new_user()

    def test_search_user_name_using_pomchaining(self,page: Page):
        page.goto(login_url)
        demo = DemoLoginPage(page)
        demo.enter_username("admin").enter_password("admin").click_sign_in().click_admin_more_info().click_search().enter_username("ann123").select_usertype().click_search_user()

#Allure Report is an open-source framework-agnostic test result visualization tool.
# it is developed by Qameta Software along with open-source community contributors
# It transforms test execution data into clear, interactive HTML reports.
# It works with popular testing frameworks across JavaScript, Python, Java, C#, PHP, and Ruby, helping teams track test results and better manage software quality.


