"""
This page contains methods that I can use many times in order to re use the code.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():

    # Initializer
    def __init__(self, driver):
        self.driver = driver

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def waitForElementEnable(self, by_locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def waitForElementVisible(self, by_locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def typeOnElement(self, by_locator, text):
        self.driver.find_element(*by_locator).clear()
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    # this function will click the web element / locator
    def clickOnElement(self, by_locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(by_locator)).click()

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, text):
        web_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(by_locator))
        assert web_element.text == text

    # this function is created to get a text from a element
    def get_text_of_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return element.text

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
