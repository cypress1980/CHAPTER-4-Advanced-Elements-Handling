from playwright.sync_api import sync_playwright
import os

def test_file_download():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to file download demo site
        page.goto("https://testing.qaautomationlabs.com/file-download.php")

        # Enter some text in the textarea
        text_to_write = "Hello, this is a Playwright download test!"
        page.fill("#textInput", text_to_write)

        # Step 1: Click "Generate File" button
        page.click("button:has-text('Generate File')")

        # Step 2: Wait for and click "Download File" link
        with page.expect_download() as download_info:
            page.click("a#downloadLink")
        download = download_info.value

        # Step 3: Save the downloaded file
        os.makedirs("downloads", exist_ok=True)
        file_path = os.path.join("downloads", "playwright_test_file.txt")
        download.save_as(file_path)
        page.wait_for_timeout(5000)
        print(f"Downloaded file name: {download.suggested_filename}")
        browser.close()