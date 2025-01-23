from utils.helpers import *
import time

def task1(driver):

    print("Task 1: Starting...")
    time.sleep(5)
    # Step 1: Scroll down
    scroll_to_bottom(driver)

    time.sleep(1)

    # Step 2: Click on icons : My Lists, History and Nearby
    icons = ["My lists", "History", "Nearby"]
    for icon in icons:
        print(f"Clicking on the icon: {icon}")
        element = wait_for_element(
            driver, (By.XPATH, f"//android.widget.FrameLayout[@content-desc='{icon}']")
        )
        element.click()
        time.sleep(3)

    # Step 3: Click on the "Explore" icon
    print("Returning to the Explore section...")
    explore_icon = wait_for_element(
        driver, (By.XPATH, "//android.widget.FrameLayout[@content-desc='Explore']")
    )
    explore_icon.click()

    # Step 4: Scroll back to the top
    print("Scrolling to the top of the page until no more content...")
    scroll_to_top(driver)
    scroll_to_top(driver)
    time.sleep(1)
    print("Task 1: Completed successfully!")
