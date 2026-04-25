import pytest
from playwright.sync_api import Page, expect
from tests.ui.pages.home_page import HomePage


@pytest.mark.smoke
@pytest.mark.ui
class TestHomePage:

    def test_homepage_loads(self, page: Page):
        home = HomePage(page)
        home.navigate()
        expect(page).to_have_title("Automation Exercise")

    def test_homepage_slider_visible(self, page: Page):
        home = HomePage(page)
        home.navigate()
        home.assert_page_loaded()

    def test_homepage_navigation_links_present(self, page: Page):
        home = HomePage(page)
        home.navigate()
        expect(home.nav_products).to_be_visible()
        expect(home.nav_cart).to_be_visible()
        expect(home.nav_signup_login).to_be_visible()

    def test_navigate_to_products(self, page: Page):
        home = HomePage(page)
        home.navigate()
        home.go_to_products()
        expect(page).to_have_url("/products")
