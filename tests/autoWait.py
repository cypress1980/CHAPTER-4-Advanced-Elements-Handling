from playwright.sync_api import sync_playwright
def test_auto_wait():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Go to a demo website (DuckDuckGo search engine)
        print("Opening the website...")
        page.goto("https://amazon.in/")

        # Type a search term in the search box
        print("Typing 'Python coding for kids' into the search box...")
        
        # Auto-Waiting happens here: Playwright waits for the search box to be ready
        page.fill("#twotabsearchtextbox", "Playwright")
        # Click the search button
        print("Clicking the search button...")
        
        # Auto-Waiting happens here: Playwright waits for the button to be clickable
        page.click("input[type='submit']")
        
        # Wait a moment to see the results
        page.wait_for_timeout(3000)  # Wait 3 seconds to observe

        # Close the browser
        print("Closing the browser...")
        browser.close()