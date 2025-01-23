from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.capabilities import get_desired_capabilities
from tasks.task1 import task1
from tasks.task2 import task2
from tasks.task3 import task3

if __name__ == "__main__":
    # Get desired capabilities
    capabilities = get_desired_capabilities()
    print("Capabilities:", capabilities)  # Debugging: Print capabilities

    # Convert capabilities to UiAutomator2Options
    options = UiAutomator2Options()
    options.platform_name = capabilities["platformName"]
    options.platform_version = capabilities["platformVersion"]
    options.device_name = capabilities["deviceName"]
    options.app = capabilities["app"]
    options.automation_name = capabilities["automationName"]

    # Initialize Appium driver
    driver = webdriver.Remote(
        command_executor="http://localhost:4723/wd/hub",
        options=options
    )

    try:
        # Execute tasks
        print("Starting Task 1...")
        task1(driver)
        print("Task 1 completed!")

        print("Starting Task 2...")
        task2(driver)
        print("Task 2 completed!")

        print("Starting Task 3...")
        task3(driver)
        print("Task 3 completed!")

    finally:
        driver.quit()
