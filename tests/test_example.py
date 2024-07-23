# pytest tests/test_example.py

import pytest
from playwright.async_api import async_playwright, expect
from config import playwright_config

@pytest.mark.asyncio
async def test_example_async_2():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=playwright_config.config["headless"])
        page = await browser.new_page()
        await page.goto(playwright_config.config["base_url"])
        await expect(page.locator("#header-container")).to_contain_text("Hello I'm Robbert")
        await browser.close()