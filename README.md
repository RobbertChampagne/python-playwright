# python-playwright

### Virtual Environments in Anaconda:
Create a New Anaconda Environment:
```Bash
conda create --name python-playwrightenv python=3.11
```
 To activate this environment, use:
```Bash
conda activate python-playwrightenv
```
To deactivate an active environment, use
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