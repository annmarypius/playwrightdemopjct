from playwright.sync_api import Page,expect
from constants.constant import login_url
from utilities.excel_read import NewExcelReader
from Pages.saucedemo_login_page import PomLoginPage
from Pages.demo_login_page import DemoLoginPage
import pytest
class TestLogin:
    def test_valid_login(self,page: Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.get_by_text("Sign In").click()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")

    def test_valid_login_excel(self,page: Page):
        page.goto(login_url)
        obj=NewExcelReader()
        username=obj.read_excel_cell(2,1)
        password=obj.read_excel_cell(2,2)
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.get_by_text("Sign In").click()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")
    #@pytest.mark.flaky(rerun=5)
    @pytest.mark.sanity
    def test_invalid_login(self,page: Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("1234")
        page.get_by_text("Sign In").click()
        alert_class=page.locator(".alert alert-danger alert-dismissible")
        expect(alert_class).to_contain_text("Invalid Username/Password")

    def test_valid_login_excel(self,page: Page):
        page.goto(login_url)
        obj=NewExcelReader()
        username=obj.read_excel_cell(3,1)
        password=obj.read_excel_cell(3,2)
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.get_by_text("Sign In").click()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin")

    def test_admin_dashboard(self,page: Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.get_by_text("Sign In").click()
        slides=page.locator(".col-lg-3 col-6")
        count=slides.count()
        expect(slides).to_have_count(count)
        #expect(slides).to_have_count(10)

    def test_admin_logout(self,page: Page):
        page.goto(login_url)
        page.get_by_placeholder("Username").fill("admin")
        page.get_by_placeholder("Password").fill("admin")
        page.locator("//button[text()='Sign In']").click()
        page.locator("a[data-toggle='dropdown']").click()#admin icon
        page.locator("a[class='dropdown-item']").nth(1).click()#logout option
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin/login")
#######################################################################################
    #test cases using POM
#new site https://www.saucedemo.com/

    @pytest.mark.order(2)
    def test_saucedemo_login_pom(self,page:Page):
        page.goto("https://www.saucedemo.com/")
        log=PomLoginPage(page)#object createdand fixture passing,constructor gets called while creating object
        log.enter_username("standard_user")#argument
        log.enter_password("secret_sauce")
        log.click_login()

#using demo project
    @pytest.mark.order(1)
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_login_pom(self,page: Page):
        page.goto(login_url)
        demo=DemoLoginPage(page)
        demo.enter_username("admin")
        demo.enter_password("admin")
        page.screenshot(path="screenshots/image1.png")
        demo.click_sign_in()
        page.screenshot(path="screenshots/image2.png")
     #using pom chaining-using login pom alone

    def test_valid_admin_login_with_pomchaining(self,page: Page):
        page.goto(login_url)
        demo=DemoLoginPage(page)
        demo.enter_username("").enter_password("").click_sign_in()

    #using pom chaining for logout-connecting login pom and admin dashboard pom
    def test_valid_admin_logout_withpomchaining(self,page: Page):
        page.goto(login_url)
        demo=DemoLoginPage(page)
        demo.enter_username("admin").enter_password("admin").click_sign_in().click_admin_icon().click_logout()
        expect(page).to_have_url("https://groceryapp.uniqassosiates.com/admin/login")
    # Difference between debugging tools, screenshots, video and trace
    # Screenshot: Captures the webpage at a particular moment.  Useful for checking error messages
    # and incorrect ui elements.

    # Video Recording: Records the browser while the test runs. Useful for viewing the sequence of
    # actions leading to a success or failure.

    # Trace viewer: Records actions, network activity, dom snapshots, console information and timing details.
    # Most informative option when debugging a failed testcase.

    #Useful for viewing the sequence of actions leading to a success or failure.
    #Trace viewer:Records actions,network activity,dom snapshots,console information
    #MOst informative option while debugging a failed testcase.

    #Screenshot
    #Case1:Capture the current visible page.captures the current viewport.
    #page.screenshot(path="file.png")

    #case2 :captures the full wab page
    #captures the entire scrollable page
    # page.screenshot(path="file.png",full_page=True)

    #case3: Capture an element only(heading,button,form,table etc.)
    #page.locator("#h1").screenshot(path="file.png")
    #page.get_by_text("welcome").screenshot(path="file.png")

    #commands
    #1. pytest --screenshot=only-on-failure
    #2. pytest --screenshot=on
    #3. pytest --screenshot=off

    def test_valid_login_pom2(self,page: Page):
        page.goto(login_url)
        demo=DemoLoginPage(page)
        demo.enter_username("admin")
        demo.enter_password("admin")
        page.screenshot(path="screenshots/image1.png",full_page=True)
        demo.click_sign_in()
        page.screenshot(path="screenshots/image2.png",full_page=True)








