from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://testing.qaautomationlabs.com/drag-and-drop.php")
    
    # Selectors for the list items
    source_selector = "ul#sortableList li:has-text('Item 1')"
    target_selector = "ul#sortableList li:has-text('Item 5')"
    
    # Perform drag and drop
    page.drag_and_drop(source_selector, target_selector)
    
    # Optionally: Wait or check result
    page.wait_for_timeout(5000)
    browser.close()