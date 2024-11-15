# pytest tests/helpers/take_screenshot.py

def test_take_screenshot(main_page):
    main_page.navbar.screenshot(path='screenshots/base_screenshots/navbar.png')
