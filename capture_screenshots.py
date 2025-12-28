import time
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def capture_screenshots():
    # 1. Start Streamlit in background
    print("Starting Streamlit app...")
    process = subprocess.Popen(["streamlit", "run", "app.py", "--server.headless=true", "--server.port=8502"], 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
    
    try:
        time.sleep(5) # Wait for app to start

        # 2. Setup Driver
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1280,1024")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options=chrome_options)
        
        # 3. Access App
        print("Accessing http://localhost:8502...")
        driver.get("http://localhost:8502")
        
        # Wait for title
        WebDriverWait(driver, 10).until(EC.title_contains("Auditor"))
        
        # 4. Capture Home Screen
        time.sleep(3) # Wait for rendering
        driver.save_screenshot("screenshot_home.png")
        print("Captured screenshot_home.png")
        
        # 5. Capture Mock Execution (Simulated)
        # Assuming there is a button with specific text or we just show the upload page
        # Getting a "Mock" run might require clicking.
        # Let's try to find the "Usar Exemplo (Mock)" radio if it exists in sidebar
        # This depends on app implementation. For now, home screen is good proof.
        
    except Exception as e:
        print(f"Error capturing screenshots: {e}")
    finally:
        # Cleanup
        if 'driver' in locals():
            driver.quit()
        process.terminate()
        process.wait()
        print("Finished.")

if __name__ == "__main__":
    capture_screenshots()
