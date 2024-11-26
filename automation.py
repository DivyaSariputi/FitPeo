from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()  # Use your preferred WebDriver
driver.maximize_window()

try:
    driver.get("https://www.fitpeo.com")  # Replace with actual URL
    print("Navigated to FitPeo Homepage")

    # Wait for the Revenue Calculator link to be clickable
    calculator_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Calculator"))
    )
    calculator_link.click()
    print("Navigated to the Revenue Calculator Page")
    
    # Wait for the slider section to be visible
    slider_section = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, "slider-section-id"))  # Adjust the ID as per the element
    )
    print("Slider section found, scrolling into view")
    
    # Scroll into the slider section
    driver.execute_script("arguments[0].scrollIntoView();", slider_section)

    # Interact with the slider (if slider is an input element)
    slider = driver.find_element(By.ID, "slider-id")  # Replace with actual slider ID
    slider_value = slider.get_attribute("value")
    print("Slider value is:", slider_value)
    
    # Further actions...
    
finally:
    # Close the browser
    driver.quit()
    print("Automation completed")
