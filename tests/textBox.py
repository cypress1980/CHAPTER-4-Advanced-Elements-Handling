from playwright.sync_api import sync_playwright, expect

def test_text_box():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://shop.qaautomationlabs.com/index.php")
        
        email = page.locator('input[id="email"]')
        password = page.locator('input[id="password"]')
        
        # Assertions for email input
        expect(email).to_be_visible()
        expect(email).to_be_empty()
        expect(email).to_be_editable()
        expect(email).to_be_enabled()
        
        # Assertions for password input
        expect(password).to_be_visible()
        expect(password).to_be_empty()
        expect(password).to_be_editable()
        expect(password).to_be_enabled()
        
        # Fill login details
        email.fill("demo@demo.com")
        password.fill("demo")
        
        # Login button
        page.click('button[id="loginBtn"]')
        
        browser.close()