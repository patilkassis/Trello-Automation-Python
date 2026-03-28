import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def test_trello():
    options = Options()
    # رح نشغل وضع الـ Incognito عشان ما يتأثر بالكوكيز القديمة
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("Opening Trello...")
        driver.get("https://trello.com/home") 
        
    
        time.sleep(5) 
        
        print(f"Current Title is: {driver.title}")
        
        if "Trello" in driver.title:
            print("Test Passed: Trello is accessible!")
        else:
            print("Test Failed: Title mismatch")
            
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_trello()