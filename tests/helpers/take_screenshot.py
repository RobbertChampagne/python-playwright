# pytest tests/helpers/take_screenshot.py

from pom.main_page import MainPage

def test_take_screenshot(navigate_to_main_page):
    navigate_to_main_page.navbar.screenshot(path='screenshots/base_screenshots/navbar.png')
