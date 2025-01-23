from utils.helpers import wait_for_element
from selenium.webdriver.common.by import By
import time


def task2(driver):

    print("Task 2: Starting...")

    # Step 1: Click the search bar
    print("Activating the search bar")
    search_container = wait_for_element(driver, (By.ID, "org.wikipedia.alpha:id/search_container"))
    search_container.click()

    # Step 2: Enter "New York" in the search bar
    print("Entering 'New York' in the search bar")
    search_input = wait_for_element(driver, (By.ID, "org.wikipedia.alpha:id/search_src_text"))
    search_input.send_keys("New York")

    # Step 3: Wait for search results to load
    print("Waiting for search results to load")
    time.sleep(3)

    # Verify that the results are displayed for NEW YORK
    print("Verifying search results are displayed")
    first_result = wait_for_element(driver, (By.XPATH, "//android.widget.TextView[@text='New York City']"))
    assert first_result.is_displayed(), "Search results are not displayed!"

    # Step 4: Double-click the close button
    print("Double-clicking the close button")
    close_button = wait_for_element(driver, (By.ID, "org.wikipedia.alpha:id/search_close_btn"))
    close_button.click()
    time.sleep(0.2)
    close_button.click()


    # Verify that the app returns to home page
    print("Verifying return to home page")
    home_page_element = wait_for_element(driver, (By.ID, "org.wikipedia.alpha:id/search_container"))
    assert home_page_element.is_displayed(), "Failed to return to the home page!"

    print("Task 2: Completed successfully!")
