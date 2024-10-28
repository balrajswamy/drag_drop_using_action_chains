from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pytest
import allure


@allure.title("Action Chain TestCase #1")
@allure.description("Verify the actions ")
def test_action_chains():
    # Initialize the driver (for example, using Chrome)
    driver = webdriver.Chrome()

    # Navigate to the website
    driver.get("https://awesomeqa.com/practice.html")

    # Find the firstname element
    firstname_field = driver.find_element(By.XPATH, "//input[@name='firstname']")

    # Initialize ActionChains
    actions = ActionChains(driver = driver)

    # Type "BALRAJ" in uppercase using SHIFT key
    actions.click(firstname_field)  # Focus on the field

    # Hold SHIFT and type each letter in uppercase
    actions.key_down(Keys.SHIFT).send_keys("balraj").key_up(Keys.SHIFT).perform()

    time.sleep(3)

    # Pause for a moment to observe the result (optional)
    time.sleep(2)
    entered_text = firstname_field.get_attribute("value")
    assert entered_text == "BALRAJ", f"expected BALRAJ but got {entered_text} "

    # Close the driver
    driver.quit()
