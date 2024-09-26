# pytest tests/test_sync_basic_tests.py

from playwright.sync_api import Page, expect

def test_to_contain_text(navigate_to_main_page):
    expect(navigate_to_main_page.heading).to_contain_text("Hello I'm Robbert")
    expect(navigate_to_main_page.responsumProject).to_contain_text("Responsum T&M A software")
    expect(navigate_to_main_page.iOProject).to_contain_text("iO A end-to-end agency for")
    expect(navigate_to_main_page.mediahuisProject).to_contain_text("Mediahuis Publishing Studio")

def test_scrolling(navigate_to_main_page):
    # Get the initial scroll position
    initial_scroll_position = navigate_to_main_page.page.evaluate("window.scrollY")
    
    # Perform the click action that should trigger scrolling
    navigate_to_main_page.contactLinkNavbar.click()
    
    # Wait for any possible animations or dynamic content loading
    navigate_to_main_page.page.wait_for_timeout(1000)  # Adjust the timeout as necessary
    
    # Get the new scroll position
    new_scroll_position = navigate_to_main_page.page.evaluate("window.scrollY")
    
    # Assert that the new scroll position is greater than the initial scroll position
    assert new_scroll_position > initial_scroll_position, "The page did not scroll down after clicking."