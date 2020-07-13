import requests
import pytest
import json
from random import randrange

AUTHORIZATION_CODE = 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'
API_URL = "https://gorest.co.in/public-api/users"
FAKE_ID = "20974203928"

# ###GET##################################################################
# happy


@pytest.fixture(scope="module")
def get_request_returns_response():
    response = requests.get(
        API_URL,
        headers={
            'Authorization': AUTHORIZATION_CODE})
    return response


@pytest.fixture(scope="module")
def get_convert_response_to_json(get_request_returns_response):
    response_body = get_request_returns_response.json()
    return response_body

# negative


@pytest.fixture(scope="module")
def get_bad_request():
    response = requests.get(
        API_URL + "/" + FAKE_ID,
        headers={
            'Authorization': AUTHORIZATION_CODE})
    return response


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
        API_URL,
        headers={
            'Authorization': AUTHORIZATION_CODE},
        data=payload)
    return response


@pytest.fixture(scope="module")
def post_convert_response_to_json(post_request_returns_response):
    response_body = post_request_returns_response.json()
    return response_body

# negative


@pytest.fixture(scope="module")
def negative_post_request_returns_response(get_convert_response_to_json):
    already_used_email = get_convert_response_to_json["result"][0]["email"]
    payload = {
        "first_name": POST_FIRST_NAME,
        "last_name": POST_LAST_NAME,
        "gender": POST_GENDER,
        "email": already_used_email
    }
    response = requests.post(
        API_URL,
        headers={
            'Authorization': AUTHORIZATION_CODE},
        data=payload)
    return response


@pytest.fixture(scope="module")
def negative_post_request_returns_json(negative_post_request_returns_response):
    response_body = negative_post_request_returns_response.json()
    return response_body

# ##PUT###################################################################
# happy


@pytest.fixture(scope="module")
def return_PutData_obj():
    class PutData:
        PUT_FIRST_NAME = "Connor Mote"
        payload = {
            "first_name": PUT_FIRST_NAME
        }

        def __init__(self):
            response = requests.get(
                API_URL,
                headers={
                    'Authorization':
                        AUTHORIZATION_CODE})
            response_body = response.json()
            self.ID = response_body["result"][0]['id']

    pd = PutData()
    return pd


@pytest.fixture(scope="module")
def put_request_returns_response(return_PutData_obj):
    response = requests.put(
        API_URL + "/" + str(
            return_PutData_obj.ID),
        headers={
            'Authorization': AUTHORIZATION_CODE},
        data=return_PutData_obj.payload)
    return response


@pytest.fixture(scope="module")
def put_convert_response_to_json(put_request_returns_response):
    response_body = put_request_returns_response.json()
    return response_body

# negative


@pytest.fixture(scope="module")
def negative_put_request_returns_response(return_PutData_obj):
    response = requests.put(
        API_URL + "/" + FAKE_ID,
        headers={
            'Authorization': AUTHORIZATION_CODE},
        data=return_PutData_obj.payload)
    return response


@pytest.fixture(scope="module")
def negative_put_convert_response_to_json(
        negative_put_request_returns_response):
    response_body = negative_put_request_returns_response.json()
    return response_body


# ##DELETE##################################################################
# happy
@pytest.fixture(scope="module")
def return_DELETEData_obj():
    class DELETEData:
        def __init__(self):
            response = requests.get(
                API_URL,
                headers={
                    'Authorization':
                        AUTHORIZATION_CODE})
            response_body = response.json()
            self.ID = response_body["result"][1]['id']

    dd = DELETEData()
    return dd


@pytest.fixture(scope="module")
def delete_request_returns_response(return_DELETEData_obj):
    response = requests.delete(
        API_URL + "/" +
        return_DELETEData_obj.ID,
        headers={
            'Authorization': AUTHORIZATION_CODE})
    return response


@pytest.fixture(scope="module")
def delete_convert_response_to_json(delete_request_returns_response):
    response_body = delete_request_returns_response.json()
    return response_body

# negative


@pytest.fixture(scope="module")
def negative_delete_request_returns_response():
    response = requests.delete(
        API_URL + "/" + FAKE_ID,
        headers={
            'Authorization': AUTHORIZATION_CODE})
    return response


@pytest.fixture(scope="module")
def negative_delete_convert_response_to_json(
        negative_delete_request_returns_response):
    response_body = negative_delete_request_returns_response.json()
    return response_body
