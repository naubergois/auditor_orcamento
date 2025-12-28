import time
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def capture_full_flow():
    # 1. Start Streamlit in background
    print("Starting Streamlit app...")
    process = subprocess.Popen(["streamlit", "run", "app.py", "--server.headless=true", "--server.port=8503"], 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
    
    driver = None
    try:
        time.sleep(5) # Wait for app to start

        # 2. Setup Driver
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1600,1200") # Larger window for better screenshots
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options=chrome_options)
        
        # 3. Access App
        print("Accessing http://localhost:8503...")
        driver.get("http://localhost:8503")
        
        # Wait for app loading
        time.sleep(3) 

        # 4. Click 'Usar Exemplo (Mock)'
        print("Selecting 'Usar Exemplo (Mock)'...")
        # Streamlit radios are tricky. 
        # Strategy: Find label containing text and click it.
        # But wait, we need to click the radio option.
        # In streamlit, radios are often input elements or labels.
        # Let's try locating the label that contains "Usar Exemplo (Mock)"
        mock_labels = driver.find_elements(By.XPATH, "//label[contains(.,'Usar Exemplo (Mock)')]")
        if mock_labels:
            mock_labels[0].click()
            time.sleep(1)
        else:
            print("Warning: Could not find Mock radio, checking if button is visible directly.")

        # 5. Click 'Carregar Exemplo'
        print("Clicking 'Carregar Exemplo'...")
        # Buttons are usually buttons element
        try:
            load_btn = driver.find_element(By.XPATH, "//button[contains(.,'Carregar Exemplo')]")
            load_btn.click()
            time.sleep(2) # Wait for load message "Exemplo carregado!"
        except:
            print("Button 'Carregar Exemplo' not found or not needed.")

        # 6. Click 'Executar Auditoria Inteligente'
        print("Executing Audit...")
        run_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Executar Auditoria Inteligente')]"))
        )
        run_btn.click()
        
        # 7. Wait for Results
        print("Waiting for analysis (30s timeout)...")
        # Look for "Análise Concluída!" success message or one of the tabs
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(.,'Análise Concluída!')]"))
        )
        print("Analysis finished!")
        time.sleep(2) # Rendering wait

        # 8. Capture Results
        driver.save_screenshot("screenshot_results.png")
        print("Captured screenshot_results.png")
        
        # Capture Tabs? 
        # Tab 1 is default active.
        
    except Exception as e:
        print(f"Error capturing screenshots: {e}")
        if driver:
             driver.save_screenshot("screenshot_error.png")
    finally:
        # Cleanup
        if driver:
            driver.quit()
        process.terminate()
        process.wait()
        print("Finished.")

if __name__ == "__main__":
    capture_full_flow()
