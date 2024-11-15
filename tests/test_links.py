# pytest tests/test_links.py
# pytest tests/test_links.py --device="iPhone 13"
# pytest tests/test_links.py --device="Galaxy S9+"
# pytest tests/test_links.py::test_check_footer_link_icons8 --device="Galaxy S9+"

from playwright.sync_api import Page, expect
import pytest
from config.loggingSetup import setup_logging
import logging
import os
from config.utils import save_trace

# Setup logging configuration
logger = logging.getLogger("Links")

def test_domain_check(page_context: Page):
    try:
        # Unpack the page and context from the fixture
        main_page, context = page_context
        
        url = main_page.page.url
        assert url == 'https://robbertchampagne.com/'
        heading_text = main_page.heading.inner_text()
        assert heading_text == "Hello I'm Robbert"
        
    finally:
        # Stop tracing and save it to a file
        trace_name = 'domain_check.zip'
        trace_dir_name = 'links'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace tests/playwright/traces/{trace_dir_name}/{trace_name}")

'''
def test_subdomain_check(main_page):
    main_page.page.goto('https://www.robbertchampagne.com/')
    url = main_page.page.url
    assert url == 'https://robbertchampagne.com/'
    heading_text = main_page.heading.inner_text()
    assert heading_text == "Hello I'm Robbert"

def test_check_mediahuis_project_link(main_page):
    main_page.mediahuisProject.hover()
    with main_page.page.expect_popup() as popup_info:
        main_page.mediahuisProjectLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://www.mediahuis.be/nl/'

def test_check_io_project_link(main_page):
    main_page.iOProject.hover()
    with main_page.page.expect_popup() as popup_info:
        main_page.iOProjectLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://www.iodigital.com/nl/home'

def test_check_responsum_project_link(main_page):
    main_page.responsumProject.hover()
    with main_page.page.expect_popup() as popup_info:
        main_page.responsumProjectLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://responsum.eu/'

def test_check_footer_link_linkedin(main_page):
    with main_page.page.expect_popup() as popup_info:
        main_page.linkedinLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://www.linkedin.com/in/robbert-champagne-4565311a2'

def test_check_footer_link_github(main_page):
    with main_page.page.expect_popup() as popup_info:
        main_page.githubLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://github.com/RobbertChampagne'

def test_check_footer_link_icons8(main_page, device):
    if device == "Galaxy S9+":
        pytest.skip("Skipping test for Galaxy S9+")
    with main_page.page.expect_popup() as popup_info:
        main_page.icons8Link.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://icons8.com/'

def test_check_brightest_link(main_page):
    with main_page.page.expect_popup() as popup_info:
        main_page.brightestLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://brightest.be/'

def test_check_brightest_playwright_course_link(main_page):
    with main_page.page.expect_popup() as popup_info:
        main_page.brightestPlaywrightCourseLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://academy.brightest.be/courses/playwright/'
    '''