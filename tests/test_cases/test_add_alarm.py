import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys

def test_click_add_alarm_button(driver):
    time.sleep(5)

    # 알람 아이콘 클릭 
    icons = driver.find_elements(AppiumBy.ID, "com.google.android.deskclock:id/navigation_bar_item_icon_view")
    icons[0].click() #Alarm

    time.sleep(1)
    add_button = driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/fab")
    add_button.click()

    # 알람 추가 버튼 클릭 
    am_button =  driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/material_clock_period_am_button")
    am_button.click()

    time.sleep(1)
    # 시(hour) 설정 
    hour_button = driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/material_hour_tv")
    hour_button.click()
    hour_select = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="8 o\'clock"]')
    hour_select.click()

    time.sleep(1)
    # 분(minute) 설정 
    minute_select = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="15 minutes"]')
    minute_select.click()

    time.sleep(1)
    # ok 버튼 
    ok_button = driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/material_timepicker_ok_button")
    ok_button.click()

    time.sleep(1)
    # label 입력란 
    no_label = driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/edit_label")
    no_label.click()

    # label 입력 
    label_input = driver.find_element(AppiumBy.ID, "com.google.android.deskclock:id/label_input_field")
    label_input.send_keys("wake-up")
    driver.press_keycode(66)


