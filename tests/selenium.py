"""
Simple Selenium test script for opening a web page hosted on localhost.
"""

from selenium import webdriver

# Initialize the WebDriver (Chrome in this example)
driver = webdriver.Chrome()

# Open the web page hosted on localhost
driver.get("http://localhost:8000")  # Replace 8000 with the port your application is running on

# Wait for a few seconds to see the result
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
