from playwright.sync_api import sync_playwright, expect

def test_iframe():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the page
        page.goto("https://www.lambdatest.com/selenium-playground/iframe-demo/")

        # Locate the iframe by its id
        frame = page.frame_locator("#iFrame1")

        # Type into the contenteditable div inside the iframe
        frame.locator("div[contenteditable='true']").fill("Hello from Playwright < Python !")

        # Keep browser open for a few seconds to see result able to type or no inside iframe
        page.wait_for_timeout(5000)
        browser.close()