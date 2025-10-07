import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_headless_google_check():
    """
    Initializes a Chrome browser in headless mode, opens the Google page,
    prints the page title for verification, and then closes the browser.
    """
    print("Setting up Chrome options for headless mode...")
    
    # 1. Configure Chrome Options
    chrome_options = Options()
    
    # CRITICAL: This argument enables headless mode (no visible browser UI)
    chrome_options.add_argument("--headless")
    
    # Optional but highly recommended for robustness in headless environments
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Set a standard user-agent string to avoid detection issues
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    driver = None
    try:
        # 2. Initialize the WebDriver
        # ChromeDriverManager automatically handles downloading and setting up the correct ChromeDriver executable
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("WebDriver initialized (Headless).")
        
        # 3. Open the target page
        target_url = "https://www.google.com"
        print(f"Opening {target_url}...")
        driver.get(target_url)
        
        # Give the page a moment to load (optional, but good practice)
        time.sleep(1) 
        
        # 4. Verification and Exit
        print("\n--- Execution Results ---")
        print(f"Successfully opened page. Current URL: {driver.current_url}")
        print(f"Page Title: {driver.title}")
        print("-------------------------\n")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # 5. Clean up: ALWAYS quit the driver to free up resources
        if driver:
            driver.quit()
            print("Browser instance successfully closed and resources released.")

if __name__ == "__main__":
    run_headless_google_check()
