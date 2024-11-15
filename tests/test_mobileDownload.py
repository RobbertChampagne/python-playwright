# pytest -s tests/test_mobileDownload.py --device="iPhone 13"

def test_cv_download_on_mobile(main_page):
    # Open the menu on mobile
    main_page.mobileHamburgerMenuButton.click()

    # Start waiting for download before clicking.
    with main_page.page.expect_event('download') as download_info:
        main_page.resumeButton.click()
    download = download_info.value

    # Wait for the download process to complete and save the downloaded file somewhere.
    download.save_as('./downloads/' + download.suggested_filename)
    # Print out information about the downloaded file
    print('Downloaded file saved as:', download.suggested_filename)
    print('Downloaded from:', download.url)