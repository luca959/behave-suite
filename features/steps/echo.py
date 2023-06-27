from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import requests


@given('the application page, "{page}"')
def setup(context,page):
    context.driver=webdriver.Chrome(executable_path="/home/luca/Desktop/Testing/security_3/chromedriver")
    context.page=page

@when('an attacker tries to input the malicious {attack}')
def attack(context,attack):
    context.response=requests.get("http://localhost:4000/"+context.page+""+attack)
    context.attack = attack

@then('the application will return an alert with the "{string}" string')
def verify(context,string):
    if string in context.response.text:
        context.driver.get("http://localhost:4000/"+context.page+""+context.attack)
        try:
            WebDriverWait(context.driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

            alert = context.driver.switch_to.alert
            alert.accept()
            assert False
        except TimeoutException:
            assert True
    else:
        assert True


@then('the application will return a clickable link and an alert will appear with the "{string}" string')
def verify(context,string):
    if string in context.response.text:
        context.driver.get("http://localhost:4000/"+context.page+""+context.attack)
        myLink = context.driver.find_element(By.PARTIAL_LINK_TEXT, 'here')
        myLink.click()
        try:
            WebDriverWait(context.driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

            alert = context.driver.switch_to.alert
            alert.accept()
            assert False
        except TimeoutException:
            assert True
    else:
        assert True

