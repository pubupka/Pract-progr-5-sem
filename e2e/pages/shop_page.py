from playwright.sync_api import Page

class ShopPage:
    def __init__(self, page: Page):
        self.page = page
        self.backpack_item = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart_link = page.locator("[data-test=\"shopping-cart-link\"]")

    def add_to_cart(self) -> None:
        self.backpack_item.click()

    def go_to_cart(self) -> None:
        self.cart_link.click()
