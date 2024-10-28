import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope="module")
def driver():
    # Setup WebDriver (assuming Chrome here, adjust as necessary)
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(1)

    yield driver

    driver.quit()


@allure.story("Drag and Drop Test")
def test_drag_and_drop(driver):
    with allure.step("Open the mouse interaction page at https://awesomeqa.com/selenium/mouse_interaction.html"):
        driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
        time.sleep(3)

    with allure.step("Locate the source and target elements for drag-and-drop"):
        source_element = driver.find_element(By.XPATH, '//div[@id="draggable"]')
        target_element = driver.find_element(By.XPATH, '//div[@id="droppable"]')


    with allure.step("Perform drag and drop action using ActionChains"):
        actions = ActionChains(driver)
        actions.drag_and_drop(source_element, target_element).perform()
        time.sleep(3)

    with allure.step("Verify the drag and drop action was successful"):
        # Assuming the target element changes text or class on successful drop

        success_text = driver.find_element(By.XPATH,'//strong[@id="drop-status"]').text
        assert "dropped" in success_text, f"Expected 'dropped' in target but got {success_text}"
