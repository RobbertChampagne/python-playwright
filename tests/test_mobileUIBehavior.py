# pytest tests/test_mobileUIBehavior.py --device="iPhone 13"
# pytest tests/test_mobileUIBehavior.py::test_check_text_visible_when_hover_project --device="iPhone 13"
# playwright show-trace test-results/tests-test-mobileuibehavior-py-test-check-text-visible-when-hover-project-chromium/trace.zip
import pytest

def open_menu_and_click_link(main_page, link):
    # Open the menu on mobile
    main_page.mobileHamburgerMenuButton.click()
    # Dynamically access the link attribute
    # Will replace: main_page.skillsLinkNavbar.click()
    getattr(main_page, link).click()  
    # Wait for scroll to finish
    main_page.page.wait_for_timeout(1000)

@pytest.mark.parametrize("link, text", [
    ("projectsLinkNavbar", "Check out some of my QA"),
    ("skillsLinkNavbar", "Always a Student, Never a Master"),
    ("contactLinkNavbar", "How can I help you?")
])
def test_click_navbar_link_and_check_scroll(main_page, link, text):
    open_menu_and_click_link(main_page, link)
    # Check if the specific text is visible in the viewport
    text_visible = main_page.page.is_visible(f'text={text}')
    assert text_visible

def test_scroll_back_up_after_logo_click(main_page):
    open_menu_and_click_link(main_page, "contactLinkNavbar")
    main_page.logo.click()
    # Wait for scroll to finish
    main_page.page.wait_for_timeout(1000)
    # Check if the specific text is visible in the viewport
    text_visible = main_page.page.is_visible('text=Ensuring Software Quality')
    assert text_visible  
    
def test_click_connect_with_me_button_and_check_scroll(main_page):
    main_page.connectWithMeButton.click()
    # Wait for scroll to finish
    main_page.page.wait_for_timeout(1000)
    # Check if the specific text is visible in the viewport
    text_visible = main_page.page.is_visible('text=How can I help you?')
    assert text_visible
    
def test_check_text_visible_when_hover_project(main_page):
    projects = [
        (main_page.mediahuisProject, main_page.mediahuisProjectText, 'Mediahuis'),
        (main_page.iOProject, main_page.iOProjectText, 'iO'),
        (main_page.responsumProject, main_page.responsumProjectText, 'Responsum T&M')
    ]
    for project, project_text, expected_text in projects:
        project.hover()
        text = project_text.inner_text()
        assert expected_text in text
        
