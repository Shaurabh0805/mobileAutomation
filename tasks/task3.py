from utils.helpers import wait_for_element
from selenium.webdriver.common.by import By

def task3(driver):

    print("Task 3: Starting...")

    # Step 1: Click on 'More options'
    print("Clicking on 'More options' menu")
    more_options_button = wait_for_element(driver, (By.ID, "org.wikipedia.alpha:id/menu_overflow_button"))
    more_options_button.click()

    # Step 2: Click on 'Settings' option
    print("Navigating to 'Settings'")
    settings_option = wait_for_element(driver, (By.ID, "org.wikipedia.alpha:id/explore_overflow_settings"))
    settings_option.click()

    # Step 3: Disable all options
    print("Disabling all toggle switches")
    toggles = driver.find_elements(By.XPATH, "//android.widget.Switch")
    for toggle in toggles:
        if toggle.get_attribute("checked") == "true":
            print(f"Disabling toggle: {toggle.get_attribute('text')}")
            toggle.click()
        else:
            print(f"Toggle already disabled: {toggle.get_attribute('text')}")

    # Step 4: Close the settings page
    print("Closing setting page")
    navigate_up_button = wait_for_element(driver, (By.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']"))
    navigate_up_button.click()

    # Verify that home page is displayed
    print("Verifying home page")
    home_page_element = wait_for_element(driver, (By.ID, "org.wikipedia.alpha:id/search_container"))
    assert home_page_element.is_displayed(), "Failed to return to the home page!"

    print("Task 3: Completed successfully!")
