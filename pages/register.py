"""
This class contains all the web elements and methods found in REGISTER PAGE 
https://opencart.abstracta.us/index.php?route=account/register
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class RegisterPage(BasePage):
    # Variables
    URL = 'https://opencart.abstracta.us/index.php?route=account/register'

    # Locators / Web Elements
    first_name_field = (By.ID, 'input-firstname')
    last_name_filed = (By.ID, 'input-lastname')
    email_field = (By.ID, 'input-email')
    telephone_field = (By.ID, 'input-telephone')
    pass_field = (By.ID, 'input-password')
    conf_pass_field = (By.ID, 'input-confirm')
    terms_policy_chk = (By.XPATH, '//*[@id="content"]/form/div/div/input[1]')
    submit_button = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')

    congrats_message = (By.XPATH, '//*[@id="content"]/p[1]')
    privacy_policy_error_msg = (By.XPATH, '//*[@id="account-register"]/div[1]/text()')
    first_name_error_msg = (By.XPATH, '//*[@id="account"]/div[2]/div/div')
    last_name_error_msg = (By.XPATH, '//*[@id="account"]/div[3]/div/div')
    email_error_msg = (By.XPATH, '//*[@id="account"]/div[4]/div/div')
    telephone_error_msg = (By.XPATH, '//*[@id="account"]/div[5]/div/div')
    password_error_msg = (By.XPATH, '//*[@id="content"]/form/fieldset[2]/div[1]/div/div')
    password_error_match = (By.XPATH, '//*[@id="content"]/form/fieldset[2]/div[2]/div/div')

    # Initializer
    def __init__(self, driver):
        self.driver = driver

    # Interaction Methods
    def openPage(self):
        self.driver.get(self.URL)

    def verifyLoads(self):
        return BasePage.waitForElementEnable(self, self.first_name_field) and BasePage.waitForElementEnable(self,
                                                                                                            self.last_name_filed) and BasePage.waitForElementEnable(
            self, self.email_field) and BasePage.waitForElementEnable(self,
                                                                      self.telephone_field) and BasePage.waitForElementEnable(
            self, self.pass_field) and BasePage.waitForElementEnable(self,
                                                                     self.conf_pass_field) and BasePage.waitForElementEnable(
            self, self.terms_policy_chk) and BasePage.waitForElementEnable(self, self.submit_button)

    def typeFirstName(self, text):
        return BasePage.typeOnElement(self, self.first_name_field, text)

    def typeLastName(self, text):
        return BasePage.typeOnElement(self, self.last_name_filed, text)

    def typeEmail(self, text):
        return BasePage.typeOnElement(self, self.email_field, text)

    def typeTelephone(self, text):
        return BasePage.typeOnElement(self, self.telephone_field, text)

    def typePassword(self, text):
        return BasePage.typeOnElement(self, self.pass_field, text)

    def typeConfirmPass(self, text):
        return BasePage.typeOnElement(self, self.conf_pass_field, text)

    def clickTermsPolicy(self):
        return BasePage.clickOnElement(self, self.terms_policy_chk)

    def clickContinueButton(self):
        return BasePage.clickOnElement(self, self.submit_button)

    def congrats_msg_displayed(self):
        return BasePage.get_text_of_element(self, self.congrats_message)

    # Error msg / empty fields
    def error_first_name(self):
        return BasePage.get_text_of_element(self, self.first_name_error_msg)

    def error_last_name(self):
        return BasePage.get_text_of_element(self, self.last_name_error_msg)

    def error_email(self):
        return BasePage.get_text_of_element(self, self.email_error_msg)

    def error_telephone(self):
        return BasePage.get_text_of_element(self, self.telephone_error_msg)

    def error_password(self):
        return BasePage.get_text_of_element(self, self.password_error_msg)

    def error_policy(self):
        return BasePage.get_text_of_element(self, self.privacy_policy_error_msg)

    def error_password_no_match(self):
        return BasePage.get_text_of_element(self, self.password_error_match)
