from playwright.sync_api import sync_playwright

def test_jsAlert():
    with sync_playwright() as p:
        # Launch browser in non-headless mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/javaScript-alert.php")

        # Handle Alert
        def handle_alert(dialog):
            print("Alert text:", dialog.message)
            dialog.accept()
            output_alert = page.locator("#output").text_content()
            print("After Alert:", output_alert)
        
        page.once("dialog", handle_alert)
        page.click("button:has-text('Show Alert')")
        page.wait_for_timeout(5000)  # Wait to observe the alert

        # Handle Confirm
        def handle_confirm(dialog):
            print("Confirm text:", dialog.message)
            dialog.accept()  # Use dialog.dismiss() to cancel
       
        page.once("dialog", handle_confirm)
        page.click("button:has-text('Show Confirm')")
        output_alert = page.locator("#output").text_content()
        print("Confirm Alert:", output_alert)
        page.wait_for_timeout(5000)  # Wait to observe the confirm

        # Handle Prompt
        def handle_prompt(dialog):
            print("Prompt text:", dialog.message)
            dialog.accept("Playwright input")  # Sends input then accepts
            page.wait_for_timeout(5000)  # Wait to observe the prompt
       
        page.once("dialog", handle_prompt)
        page.click("button:has-text('Show Prompt')")
        output_alert = page.locator("#output").text_content()
        print("Prompt  Alert:", output_alert)
        page.wait_for_timeout(5000)
        # Close the browser
        browser.close()