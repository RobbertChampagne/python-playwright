# First run the test_screenshots.py file to take the base screenshot
# pytest tests/helpers/take_screenshot.py
# pytest -s tests/test_screenshots.py

import pytest
from pom.main_page import MainPage
import cv2
import numpy as np
import os

# Define your image paths (replace with actual paths)
image1_path = "screenshots/base_screenshots/navbar.png"  # Path to your reference screenshot
image2_path = "screenshots/compare_screenshots/navbar.png"  # Path where the screenshot will be saved
diff_save_path = "screenshots/diff_screenshots/diff.png"  # Path where the diff image will be saved

def take_screenshot(main_page):
    main_page.navbar.screenshot(path=image2_path)


def test_compare_images(navigate_to_main_page):
    # Take a screenshot of the current state of the main page/other element.
    take_screenshot(navigate_to_main_page)

    # Load the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Ensure the images have the same size
    if image1.shape != image2.shape:
        print("Images are not the same size.")
        return

    # Compute the absolute difference between the images
    diff = cv2.absdiff(image1, image2)

    # Convert the difference to grayscale
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale difference image
    _, thresh_diff = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)

    # Save the diff image
    cv2.imwrite(diff_save_path, thresh_diff)

    # Check if there are any differences
    if np.any(thresh_diff):
        print(f"Images are different. Difference saved at {diff_save_path}")
        assert False
    else:
        print("Images are the same.")
        assert True
