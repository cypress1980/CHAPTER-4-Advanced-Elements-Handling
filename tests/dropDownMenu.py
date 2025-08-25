from playwright.sync_api import sync_playwright

def test_shop_menu_dropdown():
    with sync_playwright() as p:
        # Launch browser in non-headless mode for visibility
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to the website
        page.goto("https://shop.qaautomationlabs.com/")
        
        # Locate the Shop menu toggle
        shop_menu = page.locator('[data-toggle="dropdown"]')
        shop_menu.wait_for(state="visible")
        
        # Test Case 1: Hover to reveal dropdown and select "Womens Wear"
        shop_menu.hover()
        #page.wait_for_timeout(3000)
        womens_wear = page.locator('a.dropdown-item:has-text("Womens Wear")')
        womens_wear.click()
        page.wait_for_url("**/womens-wear.php", timeout=10000)
        print("Navigated to Womens Wear page")
        
        # Test Case 2: Select "Electronics" from dropdown
        shop_menu.hover()
        electronics = page.locator('a.dropdown-item:has-text("Electronics")')
        electronics.click()
        page.wait_for_url("**/electronics.php")
        print("Navigated to Electronics page")
       
        
        # Test Case 3: List all dropdown items
        shop_menu.hover()
        dropdown_menu = page.locator(".dropdown-menu.show")
        dropdown_menu.wait_for(state="visible")
        dropdown_items = dropdown_menu.locator("a.dropdown-item")
        count = dropdown_items.count()
        print(f"Shop dropdown contains {count} items:")
        for i in range(count):
            item_text = dropdown_items.nth(i).text_content().strip()
            item_href = dropdown_items.nth(i).get_attribute("href")
            print(f"Item {i + 1}: {item_text} (URL: {item_href})")
        
        # Test Case 4: Select "View All" and verify
        shop_menu.hover()
        dropdown_menu.wait_for(state="visible")
        view_all = page.locator('a.dropdown-item:has-text("View All")')
        view_all.click()
        page.wait_for_url("**/shop.php")
        print("Navigated to View All page")
        
        # Close the browser
        browser.close()