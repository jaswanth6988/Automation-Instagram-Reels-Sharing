import time
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "j7223261@gmail.com"
PASSWORD = "j7223261@.com"
REEL_URL = "https://www.instagram.com/reels/DBqJOEtpeRI/"  # Replace with the reel URL
FRIEND_USERNAME = "zneo_47"  # Replace with your friend's username

# Set up ChromeDriver with the correct path (WebDriver Manager will handle this)
chrome_driver_path = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"  # Update with your downloaded path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


def random_sleep(min_time, max_time):
    """Random sleep to mimic human behavior."""
    sleep_time = random.randint(min_time, max_time)
    print(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)


def random_cursor_move():
    """Move the cursor randomly to simulate human-like behavior."""
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    pyautogui.moveTo(x, y, duration=random.uniform(0.5, 1.5))  # Random movement duration


def login_instagram():
    """Logs into Instagram using provided credentials."""
    driver.get("https://www.instagram.com/")
    random_sleep(3, 5)

    # Locate and fill the username field
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(USERNAME)
    random_cursor_move()
    random_sleep(1, 3)

    # Locate and fill the password field
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(PASSWORD)
    random_cursor_move()
    password_input.submit()
    random_sleep(3, 5)

    # Wait for login to complete
    random_sleep(5, 8)


def send_reel():
    """Navigate to a reel and send it to a friend."""
    driver.get(REEL_URL)
    random_sleep(3, 5)

    # Scroll down to make sure the Share button is visible
    driver.execute_script("window.scrollTo(0, 800);")  # Scroll more to make sure Share button is visible
    random_sleep(1, 3)

    # Wait for the Share button to be visible and clickable
    try:
        share_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Share')]"))
        )
        print("Share button found and clickable!")

        # Hover over the Share button to make it active
        actions = ActionChains(driver)
        actions.move_to_element(share_button).perform()
        random_sleep(1, 3)

        # Click the Share button
        share_button.click()
        random_sleep(1, 3)
    except Exception as e:
        print(f"Error in finding Share button: {e}")
        driver.quit()
        return

    # Search for a friend by username
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search...']")
    search_box.send_keys(FRIEND_USERNAME)
    random_sleep(1, 3)

    # Wait for the first search result to appear
    first_friend = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{FRIEND_USERNAME}')]"))
    )
    first_friend.click()  # Click on the first friend in the search results
    random_sleep(1, 3)

    # Click the Send button
    send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
    send_button.click()
    random_sleep(1, 3)


def main():
    """Main function to run the automation process."""
    login_instagram()

    try:
        while True:
            send_reel()
            print("✅ Reel sent successfully!")

            # Wait for a random time before sending the next reel (between 10 to 30 minutes)
            random_sleep(600, 1800)  # Sleep time between 10 to 30 minutes
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
