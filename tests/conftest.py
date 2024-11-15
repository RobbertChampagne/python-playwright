import pytest
from playwright.sync_api import sync_playwright, expect
from pom.main_page import MainPage
from config.browser_utils import select_browser
import logging
import sys
from pytest_html import extras
from config.html_summary import pytest_html_results_summary
from config.loggingSetup import setup_logging

# Setup logging configuration
setup_logging()
logger = logging.getLogger("Playwright")

# This fixture retrieves the value of the --device option from the command line arguments.
# So it can be used inside the tests.
@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")

# scope='session' means that the fixture is called once per test session.
# If you don't specify a scope, the fixture will be called once per test function.
@pytest.fixture(scope="function")
def page_context(pytestconfig):
    
    # Get browser name and headless option from pytest configuration
    browser_name = pytestconfig.getoption("browser")
    headless = not pytestconfig.getoption("headed")
    
    # Use Playwright to launch the browser and create a new context
    with sync_playwright() as p:
        
        # Select and launch the specified browser
        browser = select_browser(p, browser_name[0], headless)
        
        # To override the browser selection from the pytest.ini file and launch a specific browser, 
        # use the following code:
        # browser = p.chromium.launch(headless=False)
        
        # Create a new browser context (similar to a new incognito window)
        context = browser.new_context()
        
        # Start tracing to capture screenshots, snapshots, and sources
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        # Create a new page (tab) in the browser context
        page = context.new_page()
        
        page = MainPage(page)
        
        # Navigate to the specified URL
        page.navigate()
        
        # Yield the page and context to the test function
        yield page, context
        
        # Close the browser context and browser after the test is done
        context.close()
        browser.close()
    
