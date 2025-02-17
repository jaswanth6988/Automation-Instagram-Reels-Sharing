from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up ChromeDriver with the correct path
chrome_driver_path = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"  # Update path if needed
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Instagram
driver.get("https://www.instagram.com/")

input("Press Enter to exit...")  # Keep browser open for testing
driver.quit()
