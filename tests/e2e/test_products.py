import pytest
from playwright.sync_api import Page, expect
from tests.ui.pages.products_page import ProductsPage


@pytest.mark.regression
@pytest.mark.ui
class TestProducts:

    def test_products_page_loads(self, page: Page):
        products = ProductsPage(page)
        products.navigate()
        products.assert_page_loaded()

    def test_products_list_not_empty(self, page: Page):
        products = ProductsPage(page)
        products.navigate()
        assert products.get_product_count() > 0

    def test_search_returns_results(self, page: Page):
        products = ProductsPage(page)
        products.navigate()
        products.search("dress")
        expect(page.locator("h2.title:has-text('Searched Products')")).to_be_visible()
        assert products.get_product_count() > 0

    def test_search_with_no_results(self, page: Page):
        products = ProductsPage(page)
        products.navigate()
        products.search("xyznotexistingproduct123")
        assert products.get_product_count() == 0
