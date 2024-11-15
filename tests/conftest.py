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

# scope='session' means that the fixture is called once per test session.
# If you don't specify a scope, the fixture will be called once per test function.
@pytest.fixture(scope="function")
def page_context(pytestconfig):
    
    # Get browser name and headless option from pytest configuration
    browser_name = pytestconfig.getoption("browser")
    headless = not pytestconfig.getoption("headed")
    device = pytestconfig.getoption("--device")
    
    # Use the last specified browser so that command line options take precedence over pytest.ini
    browser_name = browser_name[-1]
    
    logger.info(f"Browser specified: {browser_name}")
    logger.info(f"Headless mode: {headless}")
    logger.info(f"Device specified: {device}")
    
    # Use Playwright to launch the browser and create a new context
    with sync_playwright() as p:
        
        # Check if a device is specified and the browser supports mobile emulation
        if device and browser_name == "firefox":
            logger.info("Firefox does not support mobile emulation. Switching to Chromium.")
            browser_name = "chromium"
            browser = p.chromium.launch(headless=headless)
        else:
            # Select and launch the specified browser
            browser = select_browser(p, browser_name, headless)
        
        # Check if a device is specified and the browser supports mobile emulation
        if device and browser_name in ["chromium", "webkit"]:
            device_config = p.devices[device]
            context = browser.new_context(**device_config)
        else:
            # Create a new browser context (similar to a new incognito window)
            context = browser.new_context()
        
        logger.info(f"Launching {browser_name} browser")
            
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
    
