# Automation-Instagram-Reels-Sharing
# 📢 Instagram Reel Auto-Sender (Python + Selenium)

This project automates the process of **sending Instagram Reels to a friend** at random intervals using **Python + Selenium**. The script:
- **Logs into Instagram** automatically.
- **Navigates to a specified Reel URL**.
- **Hovers over the Share button** to reveal it.
- **Searches for a friend's name and selects the first result**.
- **Clicks the Send button** to share the Reel.
- **Repeats the process at random time intervals** (10 to 30 minutes).

---

## 📌 Features
✅ **Automated Login**  
✅ **Reel Sharing to Friends**  
✅ **Randomized Timers & Cursor Movements**  
✅ **Human-like Interaction with Selenium**  
✅ **Random Friend Selection & Delay Handling**  

---

## 🔧 Installation

### 1️⃣ Install Python Dependencies  
Make sure you have **Python 3.8+** installed. Then, install the required libraries:

```sh
pip install selenium webdriver-manager pyautogui

2️⃣ Download ChromeDriver
You need to download ChromeDriver that matches your Chrome version.
Find your Chrome version:
Open Chrome → Go to Settings → About Chrome.
Download the matching ChromeDriver from this link.
Extract and move chromedriver.exe to a known location (e.g., C:\ChromeDriver\).

2️⃣ Download ChromeDriver
You need to download ChromeDriver that matches your Chrome version.
Find your Chrome version:
Open Chrome → Go to Settings → About Chrome.
Download the matching ChromeDriver from this link.
Extract and move chromedriver.exe to a known location (e.g., C:\ChromeDriver\).

3️⃣ Configure the Script
Open the script and update these variables with your Instagram details:
python:-
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"
REEL_URL = "https://www.instagram.com/reel/example_reel_id/"  # Replace with your reel URL
FRIEND_USERNAME = "friend_username_here"  # Replace with your friend's username
Also, update the path to ChromeDriver in the script:
python;-
chrome_driver_path = "C:\\ChromeDriver\\chromedriver.exe"  # Update with actual location


🚀 Running the Script
Run the script using:
sh code:-
python instagram_auto_send.py
The bot will:
Log into Instagram.
Navigate to the Reel URL.
Hover over the Share button.
Search for your friend and click the first result.
Click the Send button.
Wait for a random time (10-30 mins) and repeat.


🛠️ Troubleshooting
❌ NoSuchElementException: Share button not found
Try increasing the scroll amount in the script:
python code:-
driver.execute_script("window.scrollTo(0, 1000);")
❌ ChromeDriver Version Mismatch
Download the correct ChromeDriver version for your Chrome.
❌ Instagram Blocks the Bot
Use a VPN or different IP to avoid detection.
Add random delays to simulate human behavior.
🛡️ Disclaimer
This script is for educational purposes only. Automating actions on Instagram may violate its Terms of Service, leading to account restrictions or bans. Use it responsibly.


🌟 Contributing
Feel free to fork this repo and submit pull requests if you improve the script!

%This project is open-source

### **🚀 Next Steps**
1. **Save this as `README.md`** in your GitHub repository.
2. **Commit & Push to GitHub**:
   ```sh
   git add README.md
   git commit -m "Added README documentation"
   git push origin main
Check it on GitHub 🎉
Let me know if you want any modifications! 🚀😊









