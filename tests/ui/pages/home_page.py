from playwright.sync_api import Page, expect
from .base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.nav_signup_login = page.locator("a[href='/login']")
        self.nav_logout = page.locator("a[href='/logout']")
        self.nav_cart = page.locator("a[href='/view_cart']")
        self.nav_products = page.locator("a[href='/products']")
        self.slider_section = page.locator("#slider")
        self.features_items = page.locator(".features_items")

    def navigate(self):
        super().navigate("/")

    def go_to_login(self):
        self.nav_signup_login.click()

    def go_to_products(self):
        self.nav_products.click()

    def go_to_cart(self):
        self.nav_cart.click()

    def is_logged_in(self) -> bool:
        return self.nav_logout.is_visible()

    def assert_page_loaded(self):
        expect(self.slider_section).to_be_visible()
        expect(self.features_items).to_be_visible()
