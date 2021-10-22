from behave import *
import requests
from hamcrest import *
import re

@given(u'the battery calculation module is online and available')
def check_module(context):
    context.URL = "http://dingdata.nl/batterij"
    r = requests.get(url = context.URL)
    response = r.json()
    assert response['status'] == 'succes'


@when(u'I call the battery calculation module with {waarde_1} for {var_1} and {waarde_2} for {var_2}')
def callDualValue(context, waarde_1, var_1, waarde_2, var_2):
   upper_var_1 = var_1.upper()
   upper_var_2 = var_2.upper()
   r = requests.get(url = context.URL, params = {upper_var_1: waarde_1, upper_var_2: waarde_2})
   context.response = r.json()

@when(u'I call the battery calculation module using the following values: {waarde_1} for {var_1}, {waarde_2} for {var_2} and {waarde_3} for {var_3}')
def call_with_3_values(context, waarde_1, var_1, waarde_2, var_2, waarde_3, var_3):
   upper_var_1 = var_1.upper()
   upper_var_2 = var_2.upper()
   upper_var_3 = var_3.upper()
   r = requests.get(url = context.URL, params = {upper_var_1: waarde_1, upper_var_2: waarde_2, upper_var_3: waarde_3})
   context.response = r.json()

@then(u'The module calculates the correct value of {uitkomst}')
def step_impl(context, uitkomst):
   uitkomst = float(uitkomst)
   a = context.response
   antwoord = re.search('[^\d]*([\d.]*)[^\d]*', context.response['resultaten']['antwoord']).group(1)
   antwoord = float(antwoord)
   assert_that(antwoord, equal_to(uitkomst))