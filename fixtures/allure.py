import pytest

from tools.allure.environment import create_allure_environment_file


@pytest.fixture(scope='session', autouse=True)
def save_allure_environment_file():
    # Do nothing before the autotests start
    yield  # Autotests are executed...
    # After the autotests are completed, create the environment.properties file
    create_allure_environment_file()