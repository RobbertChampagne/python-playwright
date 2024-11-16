# pytest tests/test_sync_basic_tests.py

from playwright.sync_api import Page, expect
import logging
from config.utils import save_trace

# Setup logging configuration
logger = logging.getLogger("Basic tests")

def test_to_contain_text(page_context):
    try:
        # Unpack the page and context from the fixture
        main_page, context = page_context
    
        expect(main_page.heading).to_contain_text("Hello I'm Robbert")
        expect(main_page.responsumProject).to_contain_text("Responsum T&M A software")
        expect(main_page.iOProject).to_contain_text("iO A end-to-end agency for")
        expect(main_page.mediahuisProject).to_contain_text("Mediahuis Publishing Studio")
    finally:
        # Stop tracing and save it to a file
        trace_name = 'to_contain_text.zip'
        trace_dir_name = 'sync_basic_tests'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace traces/{trace_dir_name}/{trace_name}")

def test_scrolling(page_context):
    try:
        # Unpack the page and context from the fixture
        main_page, context = page_context
    
        # Get the initial scroll position
        initial_scroll_position = main_page.page.evaluate("window.scrollY")
        
        # Perform the click action that should trigger scrolling
        main_page.contactLinkNavbar.click()
        
        # Wait for any possible animations or dynamic content loading
        main_page.page.wait_for_timeout(1000)  # Adjust the timeout as necessary
        
        # Get the new scroll position
        new_scroll_position = main_page.page.evaluate("window.scrollY")
        
        # Assert that the new scroll position is greater than the initial scroll position
        assert new_scroll_position > initial_scroll_position, "The page did not scroll down after clicking."
    finally:
        # Stop tracing and save it to a file
        trace_name = 'scrolling.zip'
        trace_dir_name = 'sync_basic_tests'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace traces/{trace_dir_name}/{trace_name}")
