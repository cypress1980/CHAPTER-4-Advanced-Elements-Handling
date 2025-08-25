from playwright.sync_api import sync_playwright
def test_uploadFile():
 with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://testing.qaautomationlabs.com/file-upload.php")

    # Upload file to input element with id 'fileInput'
    page.set_input_files("#fileInput", "/Users/kailash.pathak/Documents/CHAPTER_4_PW_PY/pwpy.txt")
    page.wait_for_timeout(3000)

    # You can add validation code here, e.g., wait for the file name display to update
    file_info = page.inner_text("#fileInfo")
    print("Uploaded file info:", file_info)

    browser.close()