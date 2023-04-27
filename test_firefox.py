import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

base_url = 'https://homepro.herokuapp.com/index.php'
expected_url = 'https://homepro.herokuapp.com/order.php'
expected_success_url = "https://homepro.herokuapp.com/orderconfirm.php"


@pytest.mark.parametrize(("name", "lastname", "phone", "email"),
                         [
                            ("Vladimir", "LastName2", "+7-800-555-35-35", "echtopy@gmail.com"),
                            ("Anton", "LastName2", "+7-800-555-35-35", "echtopy@gmail.com"),
                            ("Mia", "LastName2", "+7-800-555-35-35", "echtopy@gmail.com"),
                            ("Crabs", "LastName2", "+7-800-555-35-35", "echtopy@gmail.com"),
                            ("Alex", "LastName2", "+7-800-555-35-35", "echtopy@gmail.com")
                        ])
@pytest.mark.regressiontest
def test_schedule_success(browser_firefox, name, lastname, phone, email):
    browser_firefox.get(base_url)
    browser_firefox.find_element(By.LINK_TEXT, "Schedule an Appointment").click()
    assert expected_url == browser_firefox.current_url
    jobtype_dropdown = Select(browser_firefox.find_element(By.NAME, "job_type"))
    jobtype_dropdown.select_by_visible_text("Decorating")
    browser_firefox.find_element(By.NAME, "first_name").send_keys(name)
    browser_firefox.find_element(By.NAME, "last_name").send_keys(lastname)
    browser_firefox.find_element(By.NAME, "phone").send_keys(phone)
    browser_firefox.find_element(By.NAME, "email").send_keys(email)
    browser_firefox.find_element(By.XPATH, "//input[@value = 'Schedule My consultation']").click()
    assert expected_success_url == browser_firefox.current_url