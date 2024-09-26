# pytest -n 6 -s tests/test_webUIBehavior.py

def test_click_projects_link_in_navbar_and_check_scroll(navigate_to_main_page):
    navigate_to_main_page.projectsLinkNavbar.click()
    # Wait for scroll to finish
    navigate_to_main_page.page.wait_for_timeout(1000)
    # Check if the specific text is visible in the viewport
    text_visible = navigate_to_main_page.page.is_visible('text=Check out some of my QA')
    assert text_visible

def test_click_skills_link_in_navbar_and_check_scroll(navigate_to_main_page):
    navigate_to_main_page.skillsLinkNavbar.click()
    # Wait for scroll to finish
    navigate_to_main_page.page.wait_for_timeout(1000)
    # Check if the specific text is visible in the viewport
    text_visible = navigate_to_main_page.page.is_visible('text=Always a Student, Never a Master')
    assert text_visible

def test_click_contact_link_in_navbar_and_check_scroll(navigate_to_main_page):
    navigate_to_main_page.contactLinkNavbar.click()
    # Wait for scroll to finish
    navigate_to_main_page.page.wait_for_timeout(1000)
    # Check if the specific text is visible in the viewport
    text_visible = navigate_to_main_page.page.is_visible('text=How can I help you?')
    assert text_visible

def test_scroll_down_then_click_logo_and_check_scroll_back_up(navigate_to_main_page):
    navigate_to_main_page.contactLinkNavbar.click()
    # Wait for scroll to finish
    navigate_to_main_page.page.wait_for_timeout(1000)

    navigate_to_main_page.logo.click()
    # Wait for scroll to finish
    navigate_to_main_page.page.wait_for_timeout(1000)
    # Check if the specific text is visible in the viewport
    text_visible = navigate_to_main_page.page.is_visible('text=Ensuring Software Quality')
    assert text_visible

def test_click_connect_with_me_button_and_check_scroll(navigate_to_main_page):
    navigate_to_main_page.connectWithMeButton.click()
    # Wait for scroll to finish
    navigate_to_main_page.page.wait_for_timeout(1000)
    # Check if the specific text is visible in the viewport
    text_visible = navigate_to_main_page.page.is_visible('text=How can I help you?')
    assert text_visible

def test_check_text_visible_when_hover_project(navigate_to_main_page):
    navigate_to_main_page.mediahuisProject.hover()
    mediahuis_project_text = navigate_to_main_page.mediahuisProjectText.inner_text()
    assert 'Mediahuis' in mediahuis_project_text

    navigate_to_main_page.iOProject.hover()
    io_project_text = navigate_to_main_page.iOProjectText.inner_text()
    assert 'iO' in io_project_text

    navigate_to_main_page.responsumProject.hover()
    responsum_project_text = navigate_to_main_page.responsumProjectText.inner_text()
    assert 'Responsum T&M' in responsum_project_text