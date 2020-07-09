import requests
import pytest
import json
from random import randrange


# ###GET##################################################################
@pytest.fixture(scope="module")
def get_request_returns_response():
    response = requests.get(
        "https://gorest.co.in/public-api/users",
        headers={
            'Authorization': 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'})
    return response


@pytest.fixture(scope="module")
def get_convert_response_to_json(get_request_returns_response):
    response_body = get_request_returns_response.json()
    return response_body


# ###POST#################################################################
POST_FIRST_NAME = "Connor"
POST_LAST_NAME = "Mote"
POST_GENDER = "male"
POST_EMAIL = "dog" + str(randrange(999999999999999)) + "@gmail.com"
payload = {
    "first_name": POST_FIRST_NAME,
    "last_name": POST_LAST_NAME,
    "gender": POST_GENDER,
    "email": POST_EMAIL
}


@pytest.fixture(scope="module")
def post_request_returns_response():
    response = requests.post(
        "https://gorest.co.in/public-api/users",
        headers={
            'Authorization': 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'},
        data=payload)
    return response


@pytest.fixture(scope="module")
def post_get_convert_response_to_json(post_request_returns_response):
    response_body = post_request_returns_response.json()
    return response_body


# ##PUT###################################################################
@pytest.fixture(scope="module")
def return_PutData_obj():
    class PutData:
        PUT_FIRST_NAME = "Connor Mote"
        payload = {
            "first_name": PUT_FIRST_NAME
        }

        def __init__(self):
            response = requests.get(
                "https://gorest.co.in/public-api/users",
                headers={
                    'Authorization':
                        'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'})
            response_body = response.json()
            self.ID = response_body["result"][0]['id']

    pd = PutData()
    return pd


@pytest.fixture(scope="module")
def put_request_returns_response(return_PutData_obj):
    response = requests.put(
        "https://gorest.co.in/public-api/users/" + str(
            return_PutData_obj.ID),
        headers={
            'Authorization': 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'},
        data=return_PutData_obj.payload)
    return response


@pytest.fixture(scope="module")
def put_get_convert_response_to_json(put_request_returns_response):
    response_body = put_request_returns_response.json()
    return response_body


# ##DELETE##################################################################
@pytest.fixture(scope="module")
def return_DELETEData_obj():
    class DELETEData:
        def __init__(self):
            response = requests.get(
                "https://gorest.co.in/public-api/users",
                headers={
                    'Authorization':
                        'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'})
            response_body = response.json()
            self.ID = response_body["result"][1]['id']

    dd = DELETEData()
    return dd


@pytest.fixture(scope="module")
def delete_request_returns_response(return_DELETEData_obj):
    response = requests.delete(
        "https://gorest.co.in/public-api/users/" +
        return_DELETEData_obj.ID,
        headers={
            'Authorization': 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'})
    return response


@pytest.fixture(scope="module")
def delete_get_convert_response_to_json(delete_request_returns_response):
    response_body = delete_request_returns_response.json()
    return response_body
