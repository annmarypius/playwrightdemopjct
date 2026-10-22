class UserPage:
    def __init__(self,page):
        self.page = page
        self.product_backpack=page.locator("//div[contains(@class,'inventory_item_name ')]")

self.popup_field_failure = page.locator("//div[contains(@class,'alert-danger')]")