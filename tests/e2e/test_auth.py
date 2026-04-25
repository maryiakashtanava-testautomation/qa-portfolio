import os
import pytest
from faker import Faker
from playwright.sync_api import Page, expect
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.home_page import HomePage

fake = Faker()


@pytest.mark.smoke
@pytest.mark.auth
class TestAuthentication:

    def test_login_page_loads(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        expect(page).to_have_title("Automation Exercise - Signup / Login")

    def test_login_with_invalid_credentials(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.login(email="invalid@test.com", password="wrongpassword")
        login.assert_login_error_visible()

    def test_signup_with_existing_email(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        # admin@admin.com is a known existing account on the site
        login.signup(name="Test User", email="admin@admin.com")
        login.assert_signup_error_visible()

    def test_successful_signup_navigates_to_registration(self, page: Page):
        login = LoginPage(page)
        login.navigate()
        login.signup(name=fake.name(), email=fake.email())
        expect(page).to_have_url("/signup")

    def test_login_with_valid_credentials(self, page: Page):
        login = LoginPage(page)
        home = HomePage(page)
        login.navigate()
        login.login(
            email=os.getenv("TEST_EMAIL"),
            password=os.getenv("TEST_PASSWORD"),
        )
        expect(page).to_have_url("/")
        assert home.is_logged_in()
