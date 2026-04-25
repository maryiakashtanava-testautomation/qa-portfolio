from playwright.sync_api import Page, expect
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_email = page.locator("input[data-qa='login-email']")
        self.login_password = page.locator("input[data-qa='login-password']")
        self.login_btn = page.locator("button[data-qa='login-button']")
        self.login_error = page.locator("p:has-text('Your email or password is incorrect!')")

        self.signup_name = page.locator("input[data-qa='signup-name']")
        self.signup_email = page.locator("input[data-qa='signup-email']")
        self.signup_btn = page.locator("button[data-qa='signup-button']")
        self.signup_error = page.locator("p:has-text('Email Address already exist!')")

    def navigate(self):
        super().navigate("/login")

    def login(self, email: str, password: str):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_btn.click()

    def signup(self, name: str, email: str):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_btn.click()

    def assert_login_error_visible(self):
        expect(self.login_error).to_be_visible()

    def assert_signup_error_visible(self):
        expect(self.signup_error).to_be_visible()
