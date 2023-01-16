import os

desired_capabilities = {
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'platformVersion': '12',
    'deviceName': os.getenv('ANDROID_DEVICE_VERSION'),
    'browserName': 'Chrome'
}

appium_server = "http://127.0.0.1:4723/wd/hub"

page_url = "https://paulcamper.com/rent-camper/"
