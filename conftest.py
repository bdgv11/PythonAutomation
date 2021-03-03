"""
This module is to create methods and reduce code. SetUp, config, etc
"""
import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope="session"):
    # Read json file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values allowed
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be user

    return config


@pytest.fixture
def driver(config):
    # Initialize webDriver instance

    if config['browser'] == "Firefox":

        b = selenium.webdriver.Firefox()
        b.maximize_window()

    elif config['browser'] == "Chrome":

        b = selenium.webdriver.Chrome()
        b.maximize_window()

    elif config['browser'] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)

    else:
        raise Exception('Browser is not supported')

    b.implicitly_wait(config['implicit_wait'])

    yield b

    # Close instance
    b.quit()
