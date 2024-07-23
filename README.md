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