import pytest,allure,requests,sys
from behave import given, when, then
sys.path.append("C:/Users/Lenovo/PycharmProjects/Prudent")

from helpers import utils
data = utils.read_yaml('datafile/search_api.yml')

@allure.feature("Test search API")
@given('The user hits the search api with valid data')
def test_search_api():
    url = data['basic']['url']

    headers = data['search_valid']['headers']

    querystring = data['search_valid']['querystring']

    response = requests.get(url, headers=headers, params=querystring)

    with allure.step("Search api hit with valid data"):
        assert response.status_code == data['search_valid']['expected_output']


@then('The user hits the search api with invalid auth')
def test_search_api_invalid_auth():
    url = data['basic']['url']

    headers = data['search_invalid_auth']['headers']

    querystring = data['search_invalid_auth']['querystring']
    response = requests.get(url, headers=headers, params=querystring)

    with allure.step("Search api hit with invalid auth"):
        assert response.status_code == data['search_invalid_auth']['expected_output']


@then('The user hits the search api without country key')
def test_search_api_without_mandatory_key():
    url = data['basic']['url']

    headers = data['search_without_mandatory']['headers']

    querystring = data['search_without_mandatory']['querystring']
    response = requests.get(url, headers=headers, params=querystring)

    with allure.step("Search api hit without mandatory key"):
        assert response.status_code == data['search_without_mandatory']['expected_output']