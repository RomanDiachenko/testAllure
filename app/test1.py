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
    assert 1 == 1

def test_2():
    print ("Something happened, dont worry, this is a test")
    assert 2 == 1
