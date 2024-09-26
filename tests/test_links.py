# pytest -s tests/test_links.py

# Using the -k option to run just one test:
# pytest -k test_check_responsum_project_link -s tests/test_links.py

def test_domain_check(navigate_to_main_page):
    url = navigate_to_main_page.page.url
    assert url == 'https://robbertchampagne.com/'
    heading_text = navigate_to_main_page.heading.inner_text()
    assert heading_text == "Hello I'm Robbert"

def test_subdomain_check(navigate_to_main_page):
    navigate_to_main_page.page.goto('https://www.robbertchampagne.com/')
    url = navigate_to_main_page.page.url
    assert url == 'https://robbertchampagne.com/'
    heading_text = navigate_to_main_page.heading.inner_text()
    assert heading_text == "Hello I'm Robbert"

def test_check_mediahuis_project_link(navigate_to_main_page):
    navigate_to_main_page.mediahuisProject.hover()
    with navigate_to_main_page.page.expect_popup() as popup_info:
        navigate_to_main_page.mediahuisProjectLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://www.mediahuis.be/nl/'

def test_check_io_project_link(navigate_to_main_page):
    navigate_to_main_page.iOProject.hover()
    with navigate_to_main_page.page.expect_popup() as popup_info:
        navigate_to_main_page.iOProjectLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://www.iodigital.com/nl/home'

def test_check_responsum_project_link(navigate_to_main_page):
    navigate_to_main_page.responsumProject.hover()
    with navigate_to_main_page.page.expect_popup() as popup_info:
        navigate_to_main_page.responsumProjectLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://responsum.eu/'

def test_check_footer_link_linkedin(navigate_to_main_page):
    with navigate_to_main_page.page.expect_popup() as popup_info:
        navigate_to_main_page.linkedinLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://www.linkedin.com/in/robbert-champagne-4565311a2'

def test_check_footer_link_github(navigate_to_main_page):
    with navigate_to_main_page.page.expect_popup() as popup_info:
        navigate_to_main_page.githubLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://github.com/RobbertChampagne'

@pytest.mark.skip(reason="Skipping test for Galaxy S9+")
def test_check_footer_link_icons8(navigate_to_main_page):
    with navigate_to_main_page.page.expect_popup() as popup_info:
        navigate_to_main_page.icons8Link.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://icons8.com/'

def test_check_brightest_link(navigate_to_main_page):
    with navigate_to_main_page.page.expect_popup() as popup_info:
        navigate_to_main_page.brightestLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://brightest.be/'

def test_check_brightest_playwright_course_link(navigate_to_main_page):
    with navigate_to_main_page.page.expect_popup() as popup_info:
        navigate_to_main_page.brightestPlaywrightCourseLink.click()
    page2 = popup_info.value
    url = page2.url
    assert url == 'https://academy.brightest.be/courses/playwright/'