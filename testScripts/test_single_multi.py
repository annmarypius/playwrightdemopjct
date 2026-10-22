from playwright.sync_api import Page, expect


class TestMiscellaneous:
    def test_single_file_upload(self, page: Page):
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        page.wait_for_timeout(3000)
        file_upload_field = page.locator("#singleFileInput")
        file_upload_field.scroll_into_view_if_needed()  # to scroll to a component
        file_upload_field.set_input_files("C:\\Users\\NETCOM\\Downloads\\Playwright\\miscellaneous test cases.txt")
        page.wait_for_timeout(3000)
        page.get_by_role("button", name="Upload Single File").click()
        page.wait_for_timeout(3000)
        result = page.locator("#singleFileStatus")
        msg = result.text_content()
        expect(result).to_be_visible()
        expect(result).to_have_text(msg)
        # here scroll_into_view_if_needed, is used t scroll the page to a said component
        # here set_input_files, is used to upload a file or image in an  input component with type="file".

    def test_multi_file_upload(self, page: Page):
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
        page.wait_for_timeout(3000)
        multi_files_upload_field = page.locator("#multipleFilesInput")
        multi_files_upload_field.scroll_into_view_if_needed()
        files = ["C:\\Users\\NETCOM\\Downloads\\Playwright\\miscellaneous test cases.txt",
                 "C:\\Users\\NETCOM\\Downloads\\JavaScript\\day3- functions.js"]
        multi_files_upload_field.set_input_files(files)
        page.get_by_role("button", name='Upload Multiple Files').click()
        result = page.locator("#multipleFilesStatus")
        msg = result.text_content()
        expect(result).to_be_visible()
        expect(result).to_have_text(msg)

        # for multi file choosing , we should upload a list inside the set_input_files()