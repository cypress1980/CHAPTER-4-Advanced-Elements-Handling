from playwright.sync_api import sync_playwright, expect

def test_radioButton():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testing.qaautomationlabs.com/radio-button.php")
        
        # Locate radio buttons by value
        male_radio = page.locator('input[type="radio"][name="gender"][value="Male"]')
        female_radio = page.locator('input[type="radio"][name="gender"][value="Female"]')
        
        # Assert radio buttons are visible and enabled
        expect(male_radio).to_be_visible()
        expect(male_radio).to_be_enabled()
        expect(female_radio).to_be_visible()
        expect(female_radio).to_be_enabled()
        
        # Select Male radio button
        male_radio.check()
        expect(male_radio).to_be_checked()
        expect(female_radio).not_to_be_checked()
        
        # Print status of radio buttons
        print("Male radio selected:", male_radio.is_checked())      # True
        print("Female radio selected:", female_radio.is_checked())  # False
        # Click the Show Selected Gender button
        page.click('button:has-text("Show Selected Gender")')
        
        # Verify result text displays "You selected: Male"
        result = page.locator('#result')
        expect(result).to_contain_text("You selected: Male")
        
        # Select Female radio button, check status, and click
        female_radio.check()
        expect(female_radio).to_be_checked()
        expect(male_radio).not_to_be_checked()
        page.click('button:has-text("Show Selected Gender")')
        expect(result).to_contain_text("You selected: Female")
        
        # Print status of radio buttons
        print("Male radio selected:", male_radio.is_checked())      # False
        print("Female radio selected:", female_radio.is_checked())  # True
        
        browser.close()
