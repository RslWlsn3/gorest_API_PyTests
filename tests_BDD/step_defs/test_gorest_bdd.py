import requests

from pytest_bdd import scenarios, given, then, parsers, scenario, when


# Scenarios

@scenario('../features/service.feature', 'Perform GET request')
def test_add():
    pass


# Given Steps

@given('GET request is performed on the gorest API')
def ddg_response():
    AUTHORIZATION_CODE = 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'
    API_URL = "https://gorest.co.in/public-api/users"
    response = requests.get(
        API_URL,
        headers={
            'Authorization': AUTHORIZATION_CODE})
    return response


# Then Steps

@then('the response status code is "200"')
def ddg_response_code(ddg_response):
    assert 200 == ddg_response.status_code