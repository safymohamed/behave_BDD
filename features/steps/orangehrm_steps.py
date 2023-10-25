import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('launch chrome browser')
def launch_browser(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install())


@when('open orangehrm homepage')
def open_webpage(context):
    context.driver.get("https://www.google.com/")
    time.sleep(10)


@then('verify that the logo present on page')
def verify_logo(context):
    status= context.driver.find_element(By.XPATH,'//img[@class="lnXdpd"]').is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()

