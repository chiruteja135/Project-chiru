import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Read data from CSV file
data = pd.read_csv('students.csv')

# Set up the webdriver
driver = webdriver.Chrome()

# Function to perform the test using data from CSV
def run_test(name, email, phone, dob, hometown):
    try:
        # Navigate to the form page
        driver.get('http://127.0.0.1:5000')

        # Fill in the form
        driver.find_element(By.ID, 'name').send_keys(name)
        driver.find_element(By.ID, 'email').send_keys(email)
        driver.find_element(By.ID, 'phone').send_keys(phone)
        driver.find_element(By.ID, 'dob').send_keys(dob)
        driver.find_element(By.ID, 'hometown').send_keys(hometown)
        time.sleep(5)  # Wait for a few seconds to see the filled form

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        # Wait for the response
        # time.sleep(3)  # Wait for a few seconds to see the submission response

        # Verify the submission message
        assert 'Data submitted successfully' in driver.page_source
        print(f"Test passed for {name}")
    except Exception as e:
        print(f"Test failed for {name}: {e}")

# Iterate through the CSV data and run tests
for index, row in data.iterrows():
    run_test(row['name'], row['email'], row['phone'], row['dob'], row['hometown'])

# Close the browser
driver.quit()

