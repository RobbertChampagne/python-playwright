# pytest tests/test_sync_example.py

import pytest
from playwright.sync_api import Page, expect
from config import playwright_config
from pom.main_page import MainPage
'''
def test_example_sync(page: Page):
    page.goto(playwright_config.config["base_url"])
    expect(page.locator("#header-container")).to_contain_text("Hello I'm Robbert")
    
@pytest.mark.skip_browser("firefox")
#@pytest.mark.only_browser("chromium")   
def test_example_sync2(page: Page):
    page.goto(playwright_config.config["base_url"])
    expect(page.locator("#header-container")).to_contain_text("Hello I'm Robbert")
    '''
    
def test_to_contain_text(navigate_to_main_page):
    expect(navigate_to_main_page.heading).to_contain_text("Hello I'm Robbert")
    '''expect(navigate_to_main_page.responsumProject).to_contain_text("Responsum T&M A software")
    expect(navigate_to_main_page.iOProject).to_contain_text("iO A end-to-end agency for")
    expect(navigate_to_main_page.mediahuisProject).to_contain_text("Mediahuis Publishing Studio")'''