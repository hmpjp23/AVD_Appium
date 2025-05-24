APPIUM_SERVER = "http://localhost:4723"

APPIUM_CAPABILITIES = {
    "platformName": "Android",
    "platformVersion": "16",
    "deviceName": "emulator-5554",
    "appPackage": "com.google.android.deskclock",
    "appActivity": "com.android.deskclock.DeskClock",
    "automationName": "UiAutomator2",
    "noReset": True,
    "newCommandTimeout": 6000,
    "autoGrantPermissions": True
    # 필요하다면 아래 옵션을 추가하세요 (지원되는 경우에만)
    # "autoAcceptAlerts": True,
    # "autoDismissAlerts": True,
    # "autoDismissConfirmations": True,
    # "autoDismissPrompts": True,
}

