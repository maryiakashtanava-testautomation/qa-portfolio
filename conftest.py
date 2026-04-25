import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Browser, BrowserContext, Page

load_dotenv(override=True)


def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://automationexercise.com")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "locale": "en-US",
        "ignore_https_errors": True,
    }


@pytest.fixture
def page(browser: Browser, base_url: str) -> Page:
    context = browser.new_context(
        base_url=base_url,
        viewport={"width": 1280, "height": 720},
    )
    context.set_default_timeout(int(os.getenv("TIMEOUT", "30000")))
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def authenticated_page(page: Page) -> Page:
    from tests.ui.pages.login_page import LoginPage
    login = LoginPage(page)
    login.navigate()
    login.login(
        email=os.getenv("TEST_EMAIL", "testuser@example.com"),
        password=os.getenv("TEST_PASSWORD", "Test@1234"),
    )
    return page
