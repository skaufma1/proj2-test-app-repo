import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup():
    chrome_driver_path = ChromeDriverManager().install()
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--headless")
    service_obj = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    yield driver
    driver.quit()

def test_signup_1(setup):
    driver = setup
    driver.get("http://54.84.147.134:5000/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "(//button[normalize-space()='Sign-in'])[1]").click()
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Bruce Springsteen")
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    message = driver.find_element(By.XPATH, "//h1[normalize-space()]").text
    assert "Welcome Bruce Springsteen" in message, "ERROR !!!"

def test_signup_2(setup):
    driver = setup
    driver.get("http://54.84.147.134:5000/")
    driver.maximize_window()
    driver.find_element(By.XPATH, "(//button[normalize-space()='Sign-in'])[1]").click()
    driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Bruce Springsteen")
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    message = driver.find_element(By.XPATH, "//h1[normalize-space()]").text
    assert "Wellcome Bruce Springsteen" in message, "ERROR !!!"