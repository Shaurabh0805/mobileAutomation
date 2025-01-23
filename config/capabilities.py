import os

def get_desired_capabilities():
    """
    Returns the desired capabilities for the Appium driver.
    """
    # Get the absolute path to the APK file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    apk_path = os.path.join(base_dir, "app", "WikipediaSample.apk")

    if not os.path.exists(apk_path):
        raise FileNotFoundError(f"APK file not found at: {apk_path}")

    # Return the desired capabilities
    return {
        "platformName": "Android",
        "platformVersion": "13",
        "deviceName": "1368443630000GC",
        "app": apk_path,
        "automationName": "UiAutomator2",
        "appPackage": "org.wikipedia",
        "appActivity": "org.wikipedia.main.MainActivity",
    }
