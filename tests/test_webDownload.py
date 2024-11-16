# pytest -s tests/test_webDownload.py
from config.utils import save_trace
import logging

# Setup logging configuration
logger = logging.getLogger("WebDownload")

def test_cv_download_on_web(page_context):
    try:
        # Unpack the page and context from the fixture
        main_page, context = page_context
        
        # Start waiting for download before clicking.
        with main_page.page.expect_event('download') as download_info:
            main_page.resumeButton.click()
        download = download_info.value

        # Wait for the download process to complete and save the downloaded file somewhere.
        download.save_as(f"./downloads/{download.suggested_filename}")
        # Print out information about the downloaded file
        logger.info(f"Downloaded file saved as: {download.suggested_filename}")
        logger.info(f"Downloaded from: {download.url}")
    
    finally:
        # Stop tracing and save it to a file
        trace_name = 'cv_download_on_web.zip'
        trace_dir_name = 'webDownload'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace traces/{trace_dir_name}/{trace_name}")
