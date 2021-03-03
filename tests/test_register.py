"""
This class contain all the tests about REGISTER PAGE
python -m pytest --html=report.html
"""
import pytest
import random

from pages.base_page import BasePage
from pages.register import RegisterPage


# ---- Test to validate the correct register for new user ----
def test_valid_register(driver):
    # Create instance for BasePage and RegisterPage
    base = BasePage(driver)
    register = RegisterPage(driver)

    # First, open the page
    register.openPage()

    # Validate that page and each field load correctly
    assert register.verifyLoads()

    # Create a random email
    letras = random.choice("abcdefghijklmnopqrstuvwxyz")
    numeros = random.randrange(1, 999)
    email = '{}{}@gmail.com'.format(letras, numeros)

    # Type on each field of the form
    register.typeFirstName("test_user")
    register.typeLastName("test_last_name")
    register.typeEmail(email)
    register.typeTelephone("88008800")
    register.typePassword("12345678")
    register.typeConfirmPass("12345678")

    # This step it's just to know a random valid email used in the test
    driver.save_screenshot("register.png")

    # Check the privacy policy
    register.clickTermsPolicy()

    # Click on continue button
    register.clickContinueButton()

    # Assert to validate that person registered correctly
    assert register.congrats_msg_displayed() == "Congratulations! Your new account has been successfully created!"


# ---- Test to validate errors when fields are empty ----
def test_validation_empty_fields(driver):
    base = BasePage(driver)
    register = RegisterPage(driver)

    register.openPage()

    assert register.verifyLoads()

    register.typeFirstName("")
    register.typeLastName("")
    register.typeEmail("")
    register.typeTelephone("")
    register.typePassword("")
    register.typeConfirmPass("")

    # Click on continue button
    register.clickContinueButton()

    assert register.error_first_name() == "First Name must be between 1 and 32 characters!"
    assert register.error_last_name() == "Last Name must be between 1 and 32 characters!"
    assert register.error_email() == "E-Mail Address does not appear to be valid!"
    assert register.error_telephone() == "Telephone must be between 3 and 32 characters!"
    assert register.error_password() == "Password must be between 4 and 20 characters!"


# ---- Test to validate error msg appear when password confirm doesn't match ----
def test_error_password_match(driver):
    # Create instance for BasePage and RegisterPage
    base = BasePage(driver)
    register = RegisterPage(driver)

    # First, open the page
    register.openPage()

    # Validate that page and each field load correctly
    assert register.verifyLoads()

    # Create a random email
    letras = random.choice("abcdefghijklmnopqrstuvwxyz")
    numeros = random.randrange(1, 999)
    email = '{}{}@gmail.com'.format(letras, numeros)

    # Type on each field of the form
    register.typeFirstName("test_user")
    register.typeLastName("test_last_name")
    register.typeEmail(email)
    register.typeTelephone("88008800")
    register.typePassword("12345678")
    register.typeConfirmPass("123456789")

    # Check the privacy policy
    register.clickTermsPolicy()

    # Click on continue button
    register.clickContinueButton()

    # Assert to validate the error msg
    assert register.error_password_no_match() == "Password confirmation does not match password!"
