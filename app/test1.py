import pytest
import allure

@allure.feature("test")
@allure.story("Test story")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test title")
@allure.description("Test description")
@allure.tag("test")
def test_test():
    print ("hello. This is test allure report")
    assert True
