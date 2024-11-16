<img src="./assets/logo.png"  width="300"/>

# Python-playwright

This is a basic setup for testing my Portfolio website.<br>
For more info on **Pytest** or **Playwright**, check out:<br> 
https://github.com/RobbertChampagne/python-testing-framework

---

### Virtual Environment:

**Run the following command to create a virtual environment:**
```Bash
python -m venv pythonenv
```

**Activate the Virtual Environment:**
```Bash
pythonenv\Scripts\activate
```

**Install Packages:**
```Bash
pip install package_name
```

**Deactivate the Virtual Environment:**
```Bash
deactivate
```

**Export the installed packages to a requirements.txt file:**
```Bash
pip freeze > requirements.txt
```

**Install packages from requirements.txt:**
```Bash
pip install -r requirements.txt
```

# Running tests

Running all tests in a file:
```Bash
pytest tests/test_links.py
```

Running a specific tests in a file:
```Bash
pytest tests/test_links.py::test_check_brightest_link
```

Running mobile emulation:
```Bash
pytest tests/test_links.py --device="Galaxy S9+"
```

Running tests on a browser other than the one specified in the `pytest.ini` file:
```Bash
pytest tests/test_links.py --browser=webkit  
```

Codegen:
```Bash
playwright codegen https://robbertchampagne.com/
```

Trace viewer:
```Bash
playwright show-trace traces/webUIBehavior/test_click_navbar_link_and_check_scroll_projectsLinkNavbar.zip
```

---

### Compare screenshots
To compare screenshots in Python, especially in the context of Playwright tests where you might not have built-in support for direct screenshot comparison, you can use an external library like OpenCV for image comparison.

**Step 1: Install OpenCV**
```Bash
pip install opencv-python
```

**Step 2: Save a Screenshot**<br>
First run the `python-playwright\tests\helpers\take_screenshot.py` file to take the base screenshot. (this can be saved for longer use)
```Bash
pytest tests/helpers/take_screenshot.py
```

**Step 3: Run the test**<br>
- Take a screenshot of the current state of the main page/other element.
- Load the images. 

    ```Python
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    ```

- Compute the absolute difference between the images.<br>
 `cv2.absdiff()` calculates the per-element absolute difference between two arrays (in this case, images).<br>
 The result is an image where each pixel value represents the absolute difference between the corresponding pixels in the input images.<br>
 The resulting `diff` image highlights the areas where the two images differ.

    ```Python
    diff = cv2.absdiff(image1, image2)
    ```

- Convert the difference to grayscale.<br>
`cv2.cvtColor()` is used to convert an image from one color space to another.<br> 
Here, `cv2.COLOR_BGR2GRAY` converts the image from Blue-Green-Red (BGR) color space to grayscale.<br>
The resulting `gray_diff` image is a single-channel image where each pixel value represents the intensity of the difference.

    ```Python
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    ```

- Threshold the grayscale difference image.<br>
`cv2.threshold()` converts a grayscale image to a binary image.<br>
The function takes four arguments:
    - The source image (`gray_diff`).
    - The threshold value (30 in this case).
    - The maximum value to use with the `THRESH_BINARY` thresholding type (255 in this case).
    - The thresholding type (`cv2.THRESH_BINARY`), which means that pixel values greater than the threshold (30) are set to the maximum value (255), and pixel values less than or equal to the threshold are set to 0.

    The resulting `thresh_diff` image is a binary image where the differences are highlighted in white (255) and the rest is black (0).

    The `_` is used to ignore the first return value of the `cv2.threshold` function.
    `cv2.threshold` returns two values:<br>
    - The threshold value that was used (which is 30 in this case).<br>
    - The thresholded image (`thresh_diff`).<br>
    
    Since the threshold value is not needed in this context, it is common practice to use `_` as a placeholder to indicate that this value is intentionally being ignored.<br>
    This makes the code cleaner and more readable.
    ```Python
    _, thresh_diff = cv2.threshold(gray_diff, 30, 255, cv2.THRESH_BINARY)
    ```
- Save the difference image<br>
`cv2.imwrite()` writes an image to a specified file.<br> 
It takes two arguments:<br>
    - The file path where the image will be saved (`diff_save_path`).<br>
    - The image to be saved (`thresh_diff`).<br>
The `thresh_diff` image is saved to the specified path, allowing you to visually inspect the differences between the two images.

    ```Python
    cv2.imwrite(diff_save_path, thresh_diff)
    ```

**Summary**
- **Compute the Absolute Difference:** Highlights pixel-wise differences between the two images.
- **Convert to Grayscale:** Simplifies the image to a single channel for easier processing.
- **Apply Threshold:** Converts the grayscale difference to a binary image, making differences more distinct.
- **Save the Image:** Stores the binary difference image for later inspection.<br>