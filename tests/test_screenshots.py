# pytest tests/test_screenshots.py

import pytest
from playwright.sync_api import sync_playwright, expect
from pom.main_page import MainPage

def test_page_screenshot(navigate_to_main_page):
    # This will take a screenshot of the navbar and compare it with a baseline image.
    #expect(navigate_to_main_page.navbar).to_have_screenshot('navbar.png') 
    # TODO compare the screenshot with a baseline image