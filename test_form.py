"""
Selenium Test Cases for Student Feedback Registration Form
==========================================================
Sub Task 4: Selenium Testing

Tests cover:
  TC-01: Check whether the form page opens successfully
  TC-02: Enter valid data and verify successful submission
  TC-03: Leave mandatory fields blank and check error messages
  TC-04: Enter invalid email format and verify validation
  TC-05: Enter invalid mobile number and verify validation
  TC-06: Check whether dropdown selection works properly
  TC-07: Check whether Submit and Reset buttons work correctly
"""

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -----------------------------------------------
#  Helper: get absolute file:// URL for index.html
# -----------------------------------------------
FORM_URL = "file:///" + os.path.abspath(
    os.path.join(os.path.dirname(__file__), "index.html")
).replace("\\", "/")

# Delay (in seconds) between each action so you can watch the tests run
STEP_DELAY = 0.8       # delay between filling each field
RESULT_DELAY = 2.0     # delay after submit to see the result
PAGE_DELAY = 1.5       # delay after loading the page


def get_driver():
    """Create and return a Chrome WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


def slow_type(element, text, delay=0.05):
    """Type text character by character so it's visible."""
    for char in text:
        element.send_keys(char)
        time.sleep(delay)


# -----------------------------------------------
#  TC-01: Check whether the form page opens successfully
# -----------------------------------------------
def test_form_page_opens(driver):
    """TC-01: The form page should open and all form elements should be present."""
    print("TC-01: Checking form page opens successfully...")

    driver.get(FORM_URL)
    time.sleep(PAGE_DELAY)

    # Check page title
    assert "Student Feedback" in driver.title, "Page title does not contain 'Student Feedback'"
    time.sleep(STEP_DELAY)

    # Check all form fields are present
    assert driver.find_element(By.ID, "studentName"), "Student Name field not found"
    time.sleep(STEP_DELAY)
    assert driver.find_element(By.ID, "emailId"), "Email ID field not found"
    time.sleep(STEP_DELAY)
    assert driver.find_element(By.ID, "mobileNumber"), "Mobile Number field not found"
    time.sleep(STEP_DELAY)
    assert driver.find_element(By.ID, "department"), "Department dropdown not found"
    time.sleep(STEP_DELAY)
    assert driver.find_element(By.ID, "genderMale"), "Gender Male radio not found"
    assert driver.find_element(By.ID, "genderFemale"), "Gender Female radio not found"
    assert driver.find_element(By.ID, "genderOther"), "Gender Other radio not found"
    time.sleep(STEP_DELAY)
    assert driver.find_element(By.ID, "feedbackComments"), "Feedback Comments field not found"
    time.sleep(STEP_DELAY)
    assert driver.find_element(By.ID, "submitBtn"), "Submit button not found"
    assert driver.find_element(By.ID, "resetBtn"), "Reset button not found"

    print("  [PASS] TC-01 PASSED: Form page opened and all elements are present.\n")
    time.sleep(RESULT_DELAY)


# -----------------------------------------------
#  TC-02: Enter valid data and verify successful submission
# -----------------------------------------------
def test_valid_submission(driver):
    """TC-02: A fully valid form should submit successfully and show success overlay."""
    print("TC-02: Testing valid form submission...")

    driver.get(FORM_URL)
    time.sleep(PAGE_DELAY)

    # Fill Student Name
    name_field = driver.find_element(By.ID, "studentName")
    slow_type(name_field, "Krishna Sharma")
    time.sleep(STEP_DELAY)

    # Fill Email
    email_field = driver.find_element(By.ID, "emailId")
    slow_type(email_field, "krishna@university.edu")
    time.sleep(STEP_DELAY)

    # Fill Mobile Number
    mobile_field = driver.find_element(By.ID, "mobileNumber")
    slow_type(mobile_field, "9876543210")
    time.sleep(STEP_DELAY)

    # Select Department
    Select(driver.find_element(By.ID, "department")).select_by_value("Computer Science")
    time.sleep(STEP_DELAY)

    # Select Gender
    driver.find_element(By.ID, "genderMale").click()
    time.sleep(STEP_DELAY)

    # Fill Feedback Comments (minimum 10 words)
    feedback_field = driver.find_element(By.ID, "feedbackComments")
    slow_type(feedback_field, "The course content was excellent and the faculty provided great guidance throughout the semester.")
    time.sleep(STEP_DELAY)

    # Click Submit
    driver.find_element(By.ID, "submitBtn").click()
    time.sleep(RESULT_DELAY)

    # Verify success overlay is visible
    success_overlay = driver.find_element(By.ID, "successOverlay")
    assert "visible" in success_overlay.get_attribute("class"), "Success overlay not shown"

    success_heading = driver.find_element(By.CSS_SELECTOR, ".success-box h2")
    assert "submitted" in success_heading.text.lower(), "Success message text incorrect"

    print("  [PASS] TC-02 PASSED: Valid form submitted successfully, success overlay displayed.\n")
    time.sleep(RESULT_DELAY)


# -----------------------------------------------
#  TC-03: Leave mandatory fields blank and check error messages
# -----------------------------------------------
def test_empty_submission(driver):
    """TC-03: Submitting an empty form should show all validation errors."""
    print("TC-03: Testing empty form submission...")

    driver.get(FORM_URL)
    time.sleep(PAGE_DELAY)

    # Click submit without filling anything
    driver.find_element(By.ID, "submitBtn").click()
    time.sleep(RESULT_DELAY)

    # Check that all error messages are visible
    name_error = driver.find_element(By.ID, "studentNameError")
    email_error = driver.find_element(By.ID, "emailIdError")
    mobile_error = driver.find_element(By.ID, "mobileNumberError")
    dept_error = driver.find_element(By.ID, "departmentError")
    gender_error = driver.find_element(By.ID, "genderError")
    feedback_error = driver.find_element(By.ID, "feedbackCommentsError")

    assert "visible" in name_error.get_attribute("class"), "Name error not shown"
    assert "visible" in email_error.get_attribute("class"), "Email error not shown"
    assert "visible" in mobile_error.get_attribute("class"), "Mobile Number error not shown"
    assert "visible" in dept_error.get_attribute("class"), "Department error not shown"
    assert "visible" in gender_error.get_attribute("class"), "Gender error not shown"
    assert "visible" in feedback_error.get_attribute("class"), "Feedback error not shown"

    # Verify success overlay is NOT shown
    success_overlay = driver.find_element(By.ID, "successOverlay")
    assert "visible" not in success_overlay.get_attribute("class"), "Success overlay should not appear"

    print("  [PASS] TC-03 PASSED: All validation errors shown on empty submission.\n")
    time.sleep(RESULT_DELAY)


# -----------------------------------------------
#  TC-04: Enter invalid email format and verify validation
# -----------------------------------------------
def test_invalid_email(driver):
    """TC-04: Entering an invalid email format should show an email error."""
    print("TC-04: Testing invalid email format...")

    driver.get(FORM_URL)
    time.sleep(PAGE_DELAY)

    # Fill all fields correctly except email
    slow_type(driver.find_element(By.ID, "studentName"), "John Doe")
    time.sleep(STEP_DELAY)

    slow_type(driver.find_element(By.ID, "emailId"), "invalid-email-format")
    time.sleep(STEP_DELAY)

    slow_type(driver.find_element(By.ID, "mobileNumber"), "9876543210")
    time.sleep(STEP_DELAY)

    Select(driver.find_element(By.ID, "department")).select_by_value("Information Technology")
    time.sleep(STEP_DELAY)

    driver.find_element(By.ID, "genderMale").click()
    time.sleep(STEP_DELAY)

    slow_type(driver.find_element(By.ID, "feedbackComments"),
              "This is a valid feedback comment with more than ten words in the sentence.")
    time.sleep(STEP_DELAY)

    driver.find_element(By.ID, "submitBtn").click()
    time.sleep(RESULT_DELAY)

    # Verify email error is shown
    email_error = driver.find_element(By.ID, "emailIdError")
    assert "visible" in email_error.get_attribute("class"), "Email error not shown for invalid format"
    assert "valid email" in email_error.text.lower(), "Incorrect email error message"

    # Verify success overlay is NOT shown
    success_overlay = driver.find_element(By.ID, "successOverlay")
    assert "visible" not in success_overlay.get_attribute("class"), "Success overlay should not appear"

    print("  [PASS] TC-04 PASSED: Invalid email error displayed correctly.\n")
    time.sleep(RESULT_DELAY)


# -----------------------------------------------
#  TC-05: Enter invalid mobile number and verify validation
# -----------------------------------------------
def test_invalid_mobile(driver):
    """TC-05: Entering an invalid mobile number should show a mobile error."""
    print("TC-05: Testing invalid mobile number...")

    driver.get(FORM_URL)
    time.sleep(PAGE_DELAY)

    # Fill all fields correctly except mobile number
    slow_type(driver.find_element(By.ID, "studentName"), "Jane Smith")
    time.sleep(STEP_DELAY)

    slow_type(driver.find_element(By.ID, "emailId"), "jane@example.com")
    time.sleep(STEP_DELAY)

    slow_type(driver.find_element(By.ID, "mobileNumber"), "12abc")
    time.sleep(STEP_DELAY)

    Select(driver.find_element(By.ID, "department")).select_by_value("Data Science")
    time.sleep(STEP_DELAY)

    driver.find_element(By.ID, "genderFemale").click()
    time.sleep(STEP_DELAY)

    slow_type(driver.find_element(By.ID, "feedbackComments"),
              "Great learning experience with hands-on projects and excellent mentorship from all the professors.")
    time.sleep(STEP_DELAY)

    driver.find_element(By.ID, "submitBtn").click()
    time.sleep(RESULT_DELAY)

    # Verify mobile error is shown
    mobile_error = driver.find_element(By.ID, "mobileNumberError")
    assert "visible" in mobile_error.get_attribute("class"), "Mobile error not shown for invalid number"
    assert "valid" in mobile_error.text.lower() or "10-digit" in mobile_error.text.lower(), \
        "Incorrect mobile number error message"

    # Verify success overlay is NOT shown
    success_overlay = driver.find_element(By.ID, "successOverlay")
    assert "visible" not in success_overlay.get_attribute("class"), "Success overlay should not appear"

    print("  [PASS] TC-05 PASSED: Invalid mobile number error displayed correctly.\n")
    time.sleep(RESULT_DELAY)


# -----------------------------------------------
#  TC-06: Check whether dropdown selection works properly
# -----------------------------------------------
def test_dropdown_selection(driver):
    """TC-06: The department dropdown should allow selection and reflect the chosen value."""
    print("TC-06: Testing dropdown selection...")

    driver.get(FORM_URL)
    time.sleep(PAGE_DELAY)

    dept_select = Select(driver.find_element(By.ID, "department"))

    # Verify default option is selected (empty value)
    assert dept_select.first_selected_option.get_attribute("value") == "", \
        "Default option should be empty"
    time.sleep(STEP_DELAY)

    # Select various departments and verify
    departments_to_test = [
        "Computer Science",
        "Information Technology",
        "Mechanical",
        "Data Science",
        "AI & ML"
    ]

    for dept in departments_to_test:
        dept_select.select_by_value(dept)
        time.sleep(STEP_DELAY)
        selected_value = dept_select.first_selected_option.get_attribute("value")
        assert selected_value == dept, f"Dropdown did not select '{dept}', got '{selected_value}'"
        print(f"    ✓ Selected: {dept}")

    # Verify total number of options
    all_options = dept_select.options
    assert len(all_options) >= 8, f"Expected at least 8 options, found {len(all_options)}"

    print("  [PASS] TC-06 PASSED: Dropdown selection works correctly.\n")
    time.sleep(RESULT_DELAY)


# -----------------------------------------------
#  TC-07: Check whether Submit and Reset buttons work correctly
# -----------------------------------------------
def test_buttons_functionality(driver):
    """TC-07: Submit and Reset buttons should function properly."""
    print("TC-07: Testing Submit and Reset button functionality...")

    driver.get(FORM_URL)
    time.sleep(PAGE_DELAY)

    # Fill some data
    name_field = driver.find_element(By.ID, "studentName")
    slow_type(name_field, "Test User")
    time.sleep(STEP_DELAY)

    email_field = driver.find_element(By.ID, "emailId")
    slow_type(email_field, "test@example.com")
    time.sleep(STEP_DELAY)

    mobile_field = driver.find_element(By.ID, "mobileNumber")
    slow_type(mobile_field, "1234567890")
    time.sleep(STEP_DELAY)

    Select(driver.find_element(By.ID, "department")).select_by_value("MBA")
    time.sleep(STEP_DELAY)

    driver.find_element(By.ID, "genderOther").click()
    time.sleep(STEP_DELAY)

    # Verify fields have data
    assert name_field.get_attribute("value") == "Test User", "Name field not filled"
    assert email_field.get_attribute("value") == "test@example.com", "Email field not filled"
    assert mobile_field.get_attribute("value") == "1234567890", "Mobile field not filled"

    # Click Reset Button
    print("    → Clicking Reset button...")
    driver.find_element(By.ID, "resetBtn").click()
    time.sleep(RESULT_DELAY)

    # Verify all fields are cleared after reset
    name_field = driver.find_element(By.ID, "studentName")
    email_field = driver.find_element(By.ID, "emailId")
    mobile_field = driver.find_element(By.ID, "mobileNumber")
    dept_select = Select(driver.find_element(By.ID, "department"))

    assert name_field.get_attribute("value") == "", "Name field not cleared after reset"
    assert email_field.get_attribute("value") == "", "Email field not cleared after reset"
    assert mobile_field.get_attribute("value") == "", "Mobile field not cleared after reset"
    assert dept_select.first_selected_option.get_attribute("value") == "", \
        "Department not reset to default"

    print("    ✓ Reset button working — all fields cleared")
    time.sleep(STEP_DELAY)

    # Now test Submit button with empty form (should show errors, not submit)
    print("    → Clicking Submit on empty form...")
    driver.find_element(By.ID, "submitBtn").click()
    time.sleep(RESULT_DELAY)

    name_error = driver.find_element(By.ID, "studentNameError")
    assert "visible" in name_error.get_attribute("class"), "Submit should trigger validation"

    # Success overlay should NOT be visible
    success_overlay = driver.find_element(By.ID, "successOverlay")
    assert "visible" not in success_overlay.get_attribute("class"), \
        "Success overlay should not appear on invalid submission"

    print("    ✓ Submit button triggers validation correctly")

    print("  [PASS] TC-07 PASSED: Submit and Reset buttons work correctly.\n")
    time.sleep(RESULT_DELAY)


# -----------------------------------------------
#  Main runner
# -----------------------------------------------
if __name__ == "__main__":
    driver = get_driver()

    tests = [
        test_form_page_opens,
        test_valid_submission,
        test_empty_submission,
        test_invalid_email,
        test_invalid_mobile,
        test_dropdown_selection,
        test_buttons_functionality,
    ]

    passed = 0
    failed = 0

    print("=" * 60)
    print("  Student Feedback Form - Selenium Test Suite")
    print("=" * 60 + "\n")

    for test_fn in tests:
        try:
            test_fn(driver)
            passed += 1
        except Exception as e:
            failed += 1
            print(f"  [FAIL] {test_fn.__doc__}")
            print(f"     Error: {e}\n")

    print("=" * 60)
    print(f"  Results: {passed} passed, {failed} failed out of {len(tests)} tests")
    print("=" * 60)

    driver.quit()
