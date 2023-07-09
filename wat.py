from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Function to send a message on WhatsApp
def send_whatsapp_message(phone_number, message):
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Launch Chrome
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://web.whatsapp.com')
    time.sleep(10)  # Wait for QR code scanning

    # Find the chat by phone number
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(phone_number)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Send the message
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

    # Close the browser
    driver.quit()

# Number to send reports to
phone_number = '+905393855502'

# Generate and send 100 reports
for i in range(1, 101):
    report = f"Report {i} of 100"
    send_whatsapp_message(phone_number, report)
    time.sleep(1)  # Pause to avoid getting blocked

print("All reports sent successfully!")
