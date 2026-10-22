from playwright.sync_api import Page,expect
class TestParameterisation:
    import pytest
    @pytest.mark.timeout(500)
    @pytest.mark.parametrize("validusernames",["standard_user","problem_user"])
    def test_valid_login_parameterisation(self,page:Page,validusernames):
        page.goto("https://www.saucedemo.com/")
        page.get_by_placeholder("Username").fill(validusernames)
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.locator("#login-button").click()
        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html")



