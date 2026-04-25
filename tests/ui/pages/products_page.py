from playwright.sync_api import Page, expect
from .base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.locator("input#search_product")
        self.search_btn = page.locator("button#submit_search")
        self.product_list = page.locator(".features_items")
        self.product_cards = page.locator(".productinfo")
        self.all_products_heading = page.locator("h2.title:has-text('All Products')")

    def navigate(self):
        super().navigate("/products")

    def search(self, query: str):
        self.search_input.fill(query)
        self.search_btn.click()

    def get_product_count(self) -> int:
        return self.product_cards.count()

    def add_first_product_to_cart(self):
        self.page.locator(".productinfo .btn").first.click()

    def assert_page_loaded(self):
        expect(self.all_products_heading).to_be_visible()
        expect(self.product_list).to_be_visible()
