from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.shop_page import ShopPage
from pages.checkout_step_one_page import CheckoutStepOnePage

def test_failed_order(page: Page) -> None:
    lp = LoginPage(page)
    lp.navigate()
    lp.login("standard_user", "secret_sauce")

    sp = ShopPage(page)
    sp.add_to_cart()
    sp.go_to_cart()

    cp = CartPage(page)
    cp.checkout()

    csop = CheckoutStepOnePage(page)
    csop.next_step("", "", "")

    expect(csop.error).to_contain_text("Error: First Name is required")
