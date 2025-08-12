import pytest
from utils.driver_factory import DriverFactory


@pytest.fixture()
def driver():
    driver = DriverFactory.create_driver()
    yield driver
    driver.quit()