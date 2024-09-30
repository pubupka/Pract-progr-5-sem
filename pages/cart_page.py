from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.checkout_button = page.locator("[data-test=\"checkout\"]")

    def checkout(self) -> None:
        self.checkout_button.click()
