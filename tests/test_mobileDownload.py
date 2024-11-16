# pytest tests/test_mobileDownload.py
# pytest tests/test_mobileDownload.py --device="iPhone 13"
# pytest tests/test_mobileDownload.py --device="Galaxy S9+"
# pytest tests/test_mobileDownload.py::test_cv_download_on_mobile --device="Galaxy S9+"

import logging
from config.utils import save_trace

# Setup logging configuration
logger = logging.getLogger("Downloads")

def test_cv_download_on_mobile(page_context):
    try:
        main_page, context = page_context
        
        # Open the menu on mobile
        main_page.mobileHamburgerMenuButton.click()

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
        trace_name = 'cv_download_on_mobile.zip'
        trace_dir_name = 'downloads'
        save_trace(context, trace_dir_name, trace_name)
        
        # Log the location of the trace file
        logger.info(f"Open trace: playwright show-trace traces/{trace_dir_name}/{trace_name}")
