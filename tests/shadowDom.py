from playwright.sync_api import sync_playwright, expect

def test_shadow_dom_signup_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.lambdatest.com/selenium-playground/shadow-dom", wait_until="domcontentloaded")

        # Shadow host for the form
        form_host = page.locator(".signup-form")
        expect(form_host).to_be_visible()

        # Fill the fields inside the Shadow DOM
        form_host.locator('[name="username"]').fill("play_user")
        form_host.locator('[type="email"]').fill("play_user@test.com")
        form_host.locator('[name="password"]').fill("P@ssw0rd!")
        form_host.locator('[name="confirm_password"]').fill("P@ssw0rd!")

        # Click Submit inside the shadow root)
        form_host.get_by_role("button", name="Submit").click()

        # Optional: small pause to observe
        page.wait_for_timeout(2000)
        browser.close()
