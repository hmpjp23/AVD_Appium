from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.appium_config import APPIUM_SERVER, APPIUM_CAPABILITIES

class DriverFactory:
    @staticmethod
    def get_driver():
        """
        Appium WebDriver 인스턴스를 생성하고 반환합니다.
        """
        options = UiAutomator2Options().load_capabilities(APPIUM_CAPABILITIES)
        driver = webdriver.Remote(command_executor=APPIUM_SERVER, options=options)
        driver.implicitly_wait(10)
        return driver 