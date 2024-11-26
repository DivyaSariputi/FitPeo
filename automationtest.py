from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (Chrome)
driver = webdriver.Chrome()

# Function to adjust the slider based on a specific value
def adjust_slider(slider_element, target_value):
    # Get the current slider value to calculate how much to move
    current_value = slider_element.get_attribute("value")
    current_value = float(current_value)
    
    # Calculate the adjustment required
    action = ActionChains(driver)
    
    # Move the slider to the target value
    # This assumes the slider is a horizontal input range slider
    target_offset = target_value - current_value
    if target_offset > 0:
        action.click_and_hold(slider_element).move_by_offset(target_offset * 10, 0).release().perform()
    else:
        action.click_and_hold(slider_element).move_by_offset(target_offset * 10, 0).release().perform()
    
    time.sleep(1)

# Function to perform the assignment steps
def perform_test_case():
    try:
        # Step 1: Navigate to FitPeo Homepage
        driver.get("https://www.fitpeo.com")  # Replace with the actual URL
        print("Navigated to FitPeo Homepage")
        
        # Step 2: Navigate to the Revenue Calculator Page
        calculator_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Revenue Calculator"))
        )
        calculator_link.click()
        print("Navigated to the Revenue Calculator Page")
        
        # Step 3: Scroll Down to the Slider section
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "slider-section-id"))  # Replace with the correct ID
        )
        slider_section = driver.find_element(By.ID, "slider-section-id")  # Replace with correct ID
        driver.execute_script("arguments[0].scrollIntoView();", slider_section)
        print("Scrolled to the slider section")
        
        # Step 4: Adjust the Slider to 820
        slider_element = driver.find_element(By.ID, "slider-id")  # Replace with actual slider element ID
        adjust_slider(slider_element, 820)
        
        # Step 5: Update the Text Field to 560
        text_field = driver.find_element(By.ID, "text-field-id")  # Replace with actual text field ID
        text_field.clear()
        text_field.send_keys("560")
        print("Entered 560 into the text field")
        
        # Step 6: Validate Slider Value
        WebDriverWait(driver, 10).until(
            lambda driver: slider_element.get_attribute("value") == "560"
        )
        print("Validated slider value is 560")
        
        # Step 7: Select CPT Codes
        cpt_codes = [
            "CPT-99091", "CPT-99453", "CPT-99454", "CPT-99474"
        ]
        for cpt_code in cpt_codes:
            checkbox = driver.find_element(By.ID, cpt_code)  # Replace with actual checkbox ID
            if not checkbox.is_selected():
                checkbox.click()
        print("Selected all the required CPT codes")
        
        # Step 8: Validate Total Recurring Reimbursement
        total_reimbursement = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "total-reimbursement-id"))  # Replace with actual ID
        )
        assert total_reimbursement.text == "$110700"
        print("Verified total recurring reimbursement value as $110700")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Step 9: Close the browser after completing the test
        driver.quit()
        print("Automation complete, browser closed.")

if __name__ == "__main__":
    perform_test_case()
