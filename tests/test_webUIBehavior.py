# pytest -n 6 -s tests/test_webUIBehavior.py
# pytest tests/test_webUIBehavior.py::test_click_navbar_link_and_check_scroll

import pytest
import logging
from config.utils import save_trace

# Setup logging configuration
logger = logging.getLogger("WebUIBehavior")

def click_link(main_page, link):
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
def test_click_navbar_link_and_check_scroll(page_context, link, text):
    try:
        main_page, context = page_context
        click_link(main_page, link)
        # Check if the specific text is visible in the viewport
        text_visible = main_page.page.is_visible(f'text={text}')
        assert text_visible
    finally:
        # Stop tracing and save it to a file
        trace_name = f'test_click_navbar_link_and_check_scroll_{link}.zip'
        trace_dir_name = 'webUIBehavior'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace traces/{trace_dir_name}/{trace_name}")

def test_scroll_back_up_after_logo_click(page_context):
    try:
        main_page, context = page_context
        click_link(main_page, "contactLinkNavbar")
        main_page.logo.click()
        # Wait for scroll to finish
        main_page.page.wait_for_timeout(1000)
        # Check if the specific text is visible in the viewport
        text_visible = main_page.page.is_visible('text=Ensuring Software Quality')
        assert text_visible
    finally:
        # Stop tracing and save it to a file
        trace_name = 'scroll_back_up_after_logo_click.zip'
        trace_dir_name = 'webUIBehavior'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace traces/{trace_dir_name}/{trace_name}")
    
def test_click_connect_with_me_button_and_check_scroll(page_context):
    try:
        main_page, context = page_context
        main_page.connectWithMeButton.click()
        # Wait for scroll to finish
        main_page.page.wait_for_timeout(1000)
        # Check if the specific text is visible in the viewport
        text_visible = main_page.page.is_visible('text=How can I help you?')
        assert text_visible
    finally:
        # Stop tracing and save it to a file
        trace_name = 'click_connect_with_me_button_and_check_scroll.zip'
        trace_dir_name = 'webUIBehavior'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace traces/{trace_dir_name}/{trace_name}")
        
def test_check_text_visible_when_hover_project(page_context):
    try:
        main_page, context = page_context
        projects = [
            (main_page.mediahuisProject, main_page.mediahuisProjectText, 'Mediahuis'),
            (main_page.iOProject, main_page.iOProjectText, 'iO'),
            (main_page.responsumProject, main_page.responsumProjectText, 'Responsum T&M')
        ]
        for project, project_text, expected_text in projects:
            project.hover()
            text = project_text.inner_text()
            assert expected_text in text
    finally:
        # Stop tracing and save it to a file
        trace_name = 'check_text_visible_when_hover_project.zip'
        trace_dir_name = 'webUIBehavior'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace traces/{trace_dir_name}/{trace_name}")   
