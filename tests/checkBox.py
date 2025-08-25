from playwright.sync_api import sync_playwright, expect

def test_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        
        # Log in
        page.fill('input[id="email"]', 'demo@demo.com')
        page.fill('input[id="password"]', 'demo')
        login_button = page.locator('button[id="loginBtn"]')
        login_button.click()
        
        # Click on Shop Now against Men Fashion
        # Adjust selector based on actual page content
        page.click('text=Men Fashion >> xpath=.. >> text=Shop Now')
       
        
        # Checkboxes for Formal and Footwear inside Filter by Type
        formal_checkbox = page.locator('label[for="gender-1"]')
        footwear_checkbox = page.locator('label[for="gender-2"]')
        
        # Ensure the checkboxes are visible
        expect(formal_checkbox).to_be_visible()
        expect(footwear_checkbox).to_be_visible()
        
        formal_checkbox.click()
        footwear_checkbox.click()
        # Print whether these checkboxes are checked return True
        print("Formal checkbox checked:", formal_checkbox.is_checked())
        print("Footwear checkbox checked:", footwear_checkbox.is_checked())
        page.wait_for_timeout(3000)
        
        formal_checkbox.uncheck()
        footwear_checkbox.uncheck()
        
        # You can add assertions to verify expected states after these actions
        expect(formal_checkbox).not_to_be_checked()
        expect(footwear_checkbox).not_to_be_checked()
        
        # Print whether these checkboxes are unchecked return False
        print("Formal checkbox is checked:",  formal_checkbox.is_checked())
        print("Footwear checkbox is checked:",  footwear_checkbox.is_checked())
        
        browser.close()