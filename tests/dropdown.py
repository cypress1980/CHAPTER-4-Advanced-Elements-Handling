from playwright.sync_api import sync_playwright

def test_dropdown():
    with sync_playwright() as p:
        # Launch browser in non-headless mode for visibility
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to the provided URL
        page.goto("https://testing.qaautomationlabs.com/dropdown.php")
        
        # Click on dropdown by ID
        dropdown = page.locator("#fruitDropdown")
        
        # Ensure the dropdown is visible and enabled
        dropdown.wait_for(state="visible")
        assert dropdown.is_enabled(), "Dropdown is not enabled"
        
        # Test Case 1: Select by value
        dropdown.select_option(value="Apple")
        selected_value = dropdown.input_value()
        print(f"Selected by value: {selected_value}")
        assert selected_value == "Apple", f"Expected 'Apple', but got {selected_value}"
        
        # Test Case 2: Select by label
        dropdown.select_option(label="Banana")
        selected_value = dropdown.input_value()
        print(f"Selected by label: {selected_value}")
        assert selected_value == "Banana", f"Expected 'Banana', but got {selected_value}"
        
        # Test Case 3: Select by index
        dropdown.select_option(index=2)  # Index 2 corresponds to "Banana"
        selected_value = dropdown.input_value()
        print(f"Selected by index: {selected_value}")
        assert selected_value == "Banana", f"Expected 'Banana', but got {selected_value}"
        
        # Verify all available options in the dropdown
        options = dropdown.locator("option")
        count = options.count()
        print(f"Available options ({count}):")
        for i in range(count):
            option_text = options.nth(i).text_content()
            option_value = options.nth(i).get_attribute("value")
            print(f"Option {i}: Text={option_text}, Value={option_value}")
        
        # Close the browser
        browser.close()