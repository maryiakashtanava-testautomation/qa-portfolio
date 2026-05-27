from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _dismiss_popups(self):
        try:
            self.page.get_by_role("button", name="Consent").wait_for(state="visible", timeout=3000)
            self.page.get_by_role("button", name="Consent").click()
        except Exception:
            pass
        try:
            self.page.locator("#google_vignette").wait_for(state="visible", timeout=2000)
            self.page.keyboard.press("Escape")
        except Exception:
            pass

    def navigate(self, path: str = "/"):
        self.page.goto(path)
        self._dismiss_popups()

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")

    def take_screenshot(self, name: str):
        self.page.screenshot(path=f"reports/{name}.png")
