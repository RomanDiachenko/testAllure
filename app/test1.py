import pytest
import allure

# Allure annotation for the test
@allure.title("Simple test to check assertion")
@allure.description("This test checks whether the assertion result is correct.")
@allure.severity(allure.severity_level.MINOR)  # Set the severity level
@allure.label("owner", "Roman")  # Test owner
@allure.label("team", "QA")  # Team responsible for the test
@allure.tag("example")  # Tag for the test
@allure.link("http://google.com", name="Some Link")  # Add external link
def test_example():
    # Add a step to the test
    with allure.step("Checking if numbers are equal"):
        assert 1 == 1  # Simple assertion

# Test with file attachment (e.g., image or log)
@allure.title("Test with file attachment")
@allure.description("This test adds a file with test results to the report.")
@allure.attachment("Test Results", "This could be a file or text")
def test_with_attachment():
    allure.attach("This is just a text attachment", name="Text Attachment", attachment_type=allure.attachment_type.TEXT)
    allure.attach("Additional Information", name="Additional Information", attachment_type=allure.attachment_type.JSON)
    assert True

# Annotation for specifying test steps
@allure.step("Step 1: Setup")
@allure.step("Step 2: Execution")
def test_with_steps():
    with allure.step("Check the first step"):
        assert True
    with allure.step("Check the second step"):
        assert 2 == 2

# Skipped test
@allure.title("Test that will be skipped")
@pytest.mark.skip(reason="Test skipped due to missing API")
def test_skipped():
    assert False  # This test will not run

# Test that fails
@allure.title("Test with failure")
def test_failed():
    allure.attach("Error log", "This is the error log in case of failure", attachment_type=allure.attachment_type.TEXT)
    assert 1 == 2  # This test will fail
