import pytest
from playwright.sync_api import Page
from pom.main_page import MainPage

# scope='session' means that the fixture is called once per test session.
# If you don't specify a scope, the fixture will be called once per test function.
@pytest.fixture(scope="function")
def navigate_to_main_page(page: Page):
    main_page = MainPage(page)
    main_page.navigate()
    yield main_page  # This allows the test to use the main_page object