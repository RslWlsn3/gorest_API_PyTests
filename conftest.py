import requests
import pytest
import json
from random import randrange

POST_FIRST_NAME = "Connor"
POST_LAST_NAME = "Mote"
POST_GENDER = "male"
POST_EMAIL = "dog" + str(randrange(999999999999999)) + "@gmail.com"
payload = {
    "first_name": POST_FIRST_NAME,
    "last_name" : POST_LAST_NAME,
    "gender": POST_GENDER,
    "email": POST_EMAIL
}

@pytest.fixture(scope="module")
def post_request_returns_response():    
    response = requests.post("https://gorest.co.in/public-api/users", headers={'Authorization': 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'}, data = payload)        
    return response

@pytest.fixture(scope="module")
def post_get_convert_response_to_json(post_request_returns_response):    
    response_body = post_request_returns_response.json()
    return response_body
