from playwright.sync_api import sync_playwright, expect

def test_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/dropdown.php")
        
        # Select multiple countries by value
        page.locator("#countryDropdown").select_option(["India", "UK", "Canada"])
        page.wait_for_timeout(3000)

        # Optionally verify the selection
        selected = page.locator("#countryDropdown").evaluate("el => Array.from(el.selectedOptions).map(o => o.value)")
        print("Selected options:", selected)
        browser.close()
