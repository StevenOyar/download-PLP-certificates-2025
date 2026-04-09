# download-PLP-certificates-2025
PLP Academy — Selenium Automation Script
Automates login, navigation, and certificate download on the PLP Academy platform.

Prerequisites
Python 3.13
Google Chrome browser
ChromeDriver (matching your Chrome version)
Selenium — pip install selenium

Setup
# 1. Clone or download the script
git clone  https://github.com/StevenOyar/download-PLP-certificates-2025.git
# 2. Install dependencies
pip install selenium
# 3. Ensure ChromeDriver is in your PATH
chromedriver --version
Usage
python main.py
The browser stays open after execution. Press Enter in the terminal to close it.

# What the script does
Opens powerlearnprojectafrica.org and dismisses pop-ups
Navigates to the PLP Academy in a new tab
Logs in with the provided credentials
Dismisses post-login pop-ups (profile prompt, app download prompt)
Navigates to the Certificates section in the sidebar
Views and downloads the certificate
Opens the graduation survey link



# Configuration
Update the credentials directly in the script before running:

email.send_keys("YOUR REGISTERED PLP EMAIL ADDRESS ")
password.send_keys("PLP LOGIN PASSWORD")