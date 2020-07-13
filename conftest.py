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
def GET_request_returns_response():
    response = requests.get(
        API_URL,
        headers={
            'Authorization': AUTHORIZATION_CODE})
    return response


@pytest.fixture(scope="module")
def GET_convert_response_to_json(GET_request_returns_response):
    response_body = GET_request_returns_response.json()
    return response_body

# negative


@pytest.fixture(scope="module")
def GET_fake_id():
    response = requests.get(
        API_URL + "/" + FAKE_ID,
        headers={
            'Authorization': AUTHORIZATION_CODE})
    return response

@pytest.fixture(scope="module")
def GET_bad_authorization_code():
    response = requests.get(
        API_URL,
        headers={
            'Authorization': 'Bearer VqRUbBas7UeRK3MYpC608ZRcsVVYd'})    
    return response

@pytest.fixture(scope="module")
def GET_bad_url():
    response = requests.get(
        "https://gorasdfest.co.in/public-api/users",
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
def POST_request_returns_response():
    response = requests.post(
        API_URL,
        headers={
            'Authorization': AUTHORIZATION_CODE},
        data=payload)
    return response


@pytest.fixture(scope="module")
def POST_convert_response_to_json(POST_request_returns_response):
    response_body = POST_request_returns_response.json()
    return response_body

# negative


@pytest.fixture(scope="module")
def negative_POST_request_returns_response(GET_convert_response_to_json):
    already_used_email = GET_convert_response_to_json["result"][0]["email"]
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
def negative_POST_request_returns_json(negative_POST_request_returns_response):
    response_body = negative_POST_request_returns_response.json()
    return response_body

# ##PUT###################################################################
# happy


@pytest.fixture(scope="module")
def return_PUTData_obj():
    class PUTData:
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

    pd = PUTData()
    return pd


@pytest.fixture(scope="module")
def PUT_request_returns_response(return_PUTData_obj):
    response = requests.put(
        API_URL + "/" + str(
            return_PUTData_obj.ID),
        headers={
            'Authorization': AUTHORIZATION_CODE},
        data=return_PUTData_obj.payload)
    return response


@pytest.fixture(scope="module")
def PUT_convert_response_to_json(PUT_request_returns_response):
    response_body = PUT_request_returns_response.json()
    return response_body

# negative


@pytest.fixture(scope="module")
def negative_PUT_request_returns_response(return_PUTData_obj):
    response = requests.put(
        API_URL + "/" + FAKE_ID,
        headers={
            'Authorization': AUTHORIZATION_CODE},
        data=return_PUTData_obj.payload)
    return response


@pytest.fixture(scope="module")
def negative_PUT_convert_response_to_json(
        negative_PUT_request_returns_response):
    response_body = negative_PUT_request_returns_response.json()
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
def DELETE_request_returns_response(return_DELETEData_obj):
    response = requests.delete(
        API_URL + "/" +
        return_DELETEData_obj.ID,
        headers={
            'Authorization': AUTHORIZATION_CODE})
    return response


@pytest.fixture(scope="module")
def DELETE_convert_response_to_json(DELETE_request_returns_response):
    response_body = DELETE_request_returns_response.json()
    return response_body

# negative


@pytest.fixture(scope="module")
def negative_DELETE_request_returns_response():
    response = requests.delete(
        API_URL + "/" + FAKE_ID,
        headers={
            'Authorization': AUTHORIZATION_CODE})
    return response


@pytest.fixture(scope="module")
def negative_DELETE_convert_response_to_json(
        negative_DELETE_request_returns_response):
    response_body = negative_DELETE_request_returns_response.json()
    return response_body
