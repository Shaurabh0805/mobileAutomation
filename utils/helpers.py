from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )

def scroll_to_bottom(driver):
    driver.swipe(start_x=500, start_y=1000, end_x=100, end_y=100, duration=2000)

def scroll_to_top(driver):
    driver.swipe(start_x=500, start_y=1000, end_x=500, end_y=1500, duration=2000)


def wait_for_element(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except TimeoutException:
        print(f"Element not found for locator: {locator}")
        raise
