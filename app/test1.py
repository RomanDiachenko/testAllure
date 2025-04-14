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

@allure.feature("test2")
@allure.story("Test story2")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test title2")
@allure.description("Test description2")
@allure.tag("test2")
def test_2():
    print ("Something happened, dont worry, this is a test")
    assert 2 == 1

@allure.feature("test3")
@allure.story("Test story3")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test title3")
@allure.description("Test description3")
@allure.tag("test")
@pytest.mark.skip(reason="Test3")
def test_skipped():
    assert False
