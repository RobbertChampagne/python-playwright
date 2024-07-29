<img src="./assets/logo.png"  width="300"/>

# Python-playwright

This repository provides a comprehensive toolkit for automating web interactions and visual regression testing using Playwright and Python. It includes scripts and configurations for setting up virtual environments, installing necessary dependencies, and running tests with both synchronous and asynchronous APIs.

### Features
- **Virtual Environment Setup**: Instructions for creating and managing Conda environments.
- **Playwright Installation**: Steps to install Playwright and its dependencies.
- **Sync vs Async APIs**: Detailed explanation of synchronous and asynchronous Playwright APIs.
- **Project Configuration**: Sample configurations for pytest and Playwright.
- **Screenshot Comparison**: Tools for capturing and comparing screenshots using OpenCV.

Follow the detailed steps in this README to set up and use the tools provided in this repository.

---

### Virtual Environments in Anaconda:
Create a New Anaconda Environment:
```Bash
conda create --name python-playwrightenv python=3.11
```
 To **activate** this environment, use:
```Bash
conda activate python-playwrightenv
```
or
```Bash
conda activate "C:\Program Files\Anaconda\envs\python-playwrightenv"
```
To **deactivate** an active environment, use
```Bash
conda deactivate
```
Example of the cmd:
```Bash
(python-playwrightenv) C:\...\Desktop\github\pytest>
```

To effectively recreate the environment with the correct dependencies on another device, you would typically use an `environment.yml`.<br>
Here's how you can create an `environment.yml` file and use it to recreate the environment on another device:

1. **Export Your Environment:**
    - First, ensure your Conda environment (`python-playwrightenv`) is activated.
    - Export your environment to an `environment.yml` file:

```Bash
conda env export > environment.yml
```
This file includes all the necessary information about the environment, including the name, channels from where packages are fetched, and the list of packages with their versions.

2. **Recreate the Environment on Another Device:**
    - Transfer the `environment.yml` file to the other device where you want to recreate the environment.
    - Use the following command to create an environment from the `environment.yml` file:

```Bash
conda env create -f environment.yml
```
This process ensures that you have an exact replica of your development environment on another device, including all dependencies with their correct versions.

---

### Install Playwright:
**Install the Pytest plugin:**

```Bash
pip install pytest-playwright
```

**Install the required browsers:**
```Bash
playwright install
```

---

### sync VS async:
Playwright provides two API variations to accommodate different programming styles and project requirements: <br>
synchronous (sync) and asynchronous (async). <br>
The choice between using the synchronous or asynchronous API depends on your project's context, especially regarding its concurrency model.

**Synchronous API**<br>
- **Usage**: The synchronous API is straightforward to use, <br>
especially in scripts or test frameworks that do not natively support asynchronous execution, like pytest (without additional plugins).<br>
- **How it works**: It blocks the execution of your script at each operation until the operation completes.<br>
This means that when you navigate to a page, click a button, or retrieve an element from the page, <br>
your code waits for the operation to finish before moving to the next line.<br>
- **Test Frameworks**: It's commonly used with pytest for testing because pytest's standard operation is synchronous.<br>
However, pytest can run asynchronous code with the help of plugins like pytest-asyncio.

**Asynchronous API**<br>
- **Usage**: The asynchronous API is designed for use in asynchronous environments,<br>
particularly when working with Python's asyncio library. <br>
It's beneficial in scenarios where you want to perform non-blocking operations or handle multiple I/O-bound tasks concurrently.<br>
- **How it works**: It allows your code to be non-blocking and perform other tasks while waiting for an operation to complete. <br>
This is achieved using the async and await syntax in Python, <br>
which enables the efficient management of I/O-bound and high-level structured network code.<br>
- **Test Frameworks**: For testing asynchronous code, you would typically use pytest with an async plugin like pytest-asyncio,<br> which allows pytest to run async test functions.

**Key Differences**
- **Concurrency Model**: The sync API is blocking and runs operations sequentially, <br>
while the async API is non-blocking and can run operations concurrently, <br>
making it more efficient for I/O-bound tasks.<br>
- **Syntax**: Sync API uses regular function calls, <br>
while async API requires functions to be awaited within an async function.<br>
- **Compatibility**: Sync API is simpler to use with frameworks that do not natively support async/await, <br>
whereas the async API is preferable in modern Python projects that leverage asyncio for concurrency.

---

### Project setup

`\pytest.ini`<br>
The pytest.ini file serves as a configuration file for pytest, allowing you to set default options for your test runs. <br> When pytest runs, it automatically reads options from the pytest.ini file,<br> so any options specified there apply to all test runs without needing to be explicitly included in the command line each time.
```Python
[pytest]
addopts =
    --html=report.html
    --browser=firefox
    --headed
    --tracing on
```

`\tests\conftest.py`<br>
The conftest.py file is a special pytest module that contains fixture functions, hooks, and other configurations that apply to multiple test files.<br> Pytest automatically recognizes this file and applies its contents to the tests in the same directory and subdirectories.
```Python
import pytest
from playwright.sync_api import Page
from pom.main_page import MainPage

# scope='session' means that the fixture is called once per test session.
# If you don't specify a scope, the fixture will be called once per test function.
@pytest.fixture(scope="function")
def navigate_to_main_page(page: Page):
    main_page = MainPage(page)
    main_page.navigate()
    yield main_page  # This allows the test to use the main_page object
```

`\config\playwright_config.py`<br>
The playwright_config.py file, contains configuration settings for Playwright tests.<br>
```Python
config = {
    "base_url": "https://robbertchampagne.com/",
}
```

---

### Compare screenshots
To compare screenshots in Python, especially in the context of Playwright tests where you might not have built-in support for direct screenshot comparison, you can use an external library like OpenCV for image comparison.

**Step 1: Install OpenCV**
```Bash
pip install opencv-python
```

**Step 2: Save a Screenshot**
First run the `python-playwright\tests\helpers\take_screenshot.py` file to take the base screenshot. (this can be saved for longer use)
```Bash
pytest tests/helpers/take_screenshot.py
```

**Step 3: Run the test**

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
    1. The threshold value that was used (which is 30 in this case).<br>
    2. The thresholded image (`thresh_diff`).<br>
    
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

This process effectively highlights and saves the differences between two images, making it easier to identify changes or discrepancies.