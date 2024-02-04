import pytest,allure,requests,sys
from behave import given, when, then
sys.path.append("C:/Users/Lenovo/PycharmProjects/Prudent")

from helpers import utils
data = utils.read_yaml('datafile/countries_api.yml')


@allure.feature("Test get countries API")
@given('The user hits the get countries with valid data')
def test_countries_api():
    url = data['basic']['url']

    headers = data['country_valid']['headers']

    response = requests.get(url, headers=headers)

    with allure.step("Get countries api hit with valid data"):
        assert response.status_code == data['country_valid']['expected_output']


@then('The user hits the get countries with invalid auth')
def test_search_api_invalid_auth():
    url = data['basic']['url']

    headers = data['country_invalid_auth']['headers']

    response = requests.get(url, headers=headers)

    with allure.step("Get countries api hit with invalid auth"):
        assert response.status_code == data['country_invalid_auth']['expected_output']
