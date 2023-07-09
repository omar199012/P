from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def send_whatsapp_notification(phone_number, message):
    # Launch Chrome
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com')
    time.sleep(10)  # Wait for QR code scanning

    # Find the chat by phone number
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(phone_number)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Scroll to load previous messages
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    for _ in range(4):
        message_box.send_keys(Keys.PAGE_UP)
        time.sleep(1)

    # Get the last 200 messages
    messages = driver.find_elements_by_xpath('//div[contains(@class, "message-in")]//span[contains(@class, "selectable-text")]')
    messages = messages[-200:]  # Get the last 200 messages

    # Send the notification with the messages
    notification = f"Notification for {phone_number}\n"
    for msg in messages:
        notification += f"- {msg.text}\n"

    # Send the notification message
    message_box.clear()
    message_box.send_keys(notification)
    message_box.send_keys(Keys.ENTER)

    # Close the browser
    driver.quit()

# Number to send the notification to
phone_number = "+905304928292"

# Send the notification
send_whatsapp_notification(phone_number, "Reporting the last 200 messages")

print("Notification sent successfully!")
