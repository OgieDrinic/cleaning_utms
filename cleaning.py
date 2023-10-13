#Onow this script works perfectly fine, running chromedriver selenium in the background,
#with time delay of 5s

import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_redirected_url(url, driver):
    """
    Use Selenium to open the URL and get the final redirected URL.
    """
    driver.get(url)
    time.sleep(5)  # Introduce a 5-second delay between opening each URL
    return driver.current_url

def main():
    input_filepath = '/Users/ognjendrinic/Desktop/Gumroad cleaning with Python/url.csv'
    output_filepath = '/Users/ognjendrinic/Desktop/Gumroad cleaning with Python/cleaned_url.csv'
    
    # Determine the path for chromedriver based on the current script's location
    current_directory = os.path.dirname(os.path.abspath(__file__))
    chromedriver_path = os.path.join(current_directory, 'chromedriver')
    
    # Set Chrome options for headless mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    
    # Initialize a Chrome browser instance with the specified driver path using Service object
    s = Service(chromedriver_path)
    driver = webdriver.Chrome(service=s, options=chrome_options)
    
    with open(input_filepath, 'r') as csv_file, open(output_filepath, 'w') as output_file:
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.writer(output_file)
        
        # Write header to output CSV
        csv_writer.writerow(["Original URL", "Redirected URL"])
        
        # Skip header row
        next(csv_reader)
        
        for row in csv_reader:
            original_url = row[1]  # URLs are in the second column (index 1)
            
            # Ensure the line starts with "http" before trying to fetch it
            if not original_url.startswith("http"):
                continue

            redirected_url = get_redirected_url(original_url, driver)
            csv_writer.writerow([original_url, redirected_url])
            
    # Close the browser
    driver.quit()

if __name__ == '__main__':
    main()
