import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver (assuming Chrome here, adjust as necessary)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.story("Typing uppercase text in the firstname field using ActionChains")
def test_type_uppercase_text_in_firstname(driver):
    with allure.step("Open the practice page"):
        driver.get("https://awesomeqa.com/practice.html")

    with allure.step("Locate the firstname field"):
        firstname_field = driver.find_element(By.XPATH, "//input[@name='firstname']")

    with (allure.step("Type 'BALRAJ' in uppercase using ActionChains")):
        actions = ActionChains(driver)
        #actions.click(firstname_field)  # Focus on the field
        # Hold SHIFT and type each letter in uppercase
        #actions.key_down(Keys.SHIFT).send_keys("balraj").key_up(Keys.SHIFT).perform()
        time.sleep(3)
        actions.key_down(Keys.SHIFT).send_keys_to_element(firstname_field,"balraj ponnuswamy").key_up(Keys.SHIFT).perform()
        time.sleep(3)

    with allure.step("Verify the input value"):
        entered_text = firstname_field.get_attribute("value")
        assert entered_text == "BALRAJ PONNUSWAMY", f"Expected 'BALRAJ PONNUSWAMY' but got {entered_text}"
