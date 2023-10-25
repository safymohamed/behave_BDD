import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given('I launch chrome browser')
def step_impl(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install())

@when('I open orangehrm webpage')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)


@when('I enter username "{user}" and password "{psw}"')
def step_impl(context,user,psw):
     context.driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(user)
     context.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(psw)



@when('I press the "login" button')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]').click()
    time.sleep(5)

@then(u'User can enter to dashboard page')
def step_impl(context):
     try:
         text = context.driver.find_element(By.XPATH, '//span[@class="oxd-topbar-header-breadcrumb"]').text

     except:
        context.driver.close()
        assert False, "test failed"
     if text == "Dashboard":
        context.driver.close()
        assert True, "test passed"


