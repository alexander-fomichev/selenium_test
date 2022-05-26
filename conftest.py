import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """Фикстура осуществляет инициализацию вебдрайвера Selenium"""
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(executable_path="./chromedriver", options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
