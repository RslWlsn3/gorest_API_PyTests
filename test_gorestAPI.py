import requests
import pytest
import json

#happy paths
####GET#####################################################################################################################################################
@pytest.fixture(scope="module")
def get_request_returns_response():    
    response = requests.get("https://gorest.co.in/public-api/users", headers={'Authorization': 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'})
    return response

@pytest.fixture(scope="module")
def get_convert_response_to_json(get_request_returns_response):    
    response_body = get_request_returns_response.json()
    return response_body

def test_get_check_status_code_equals_200(get_request_returns_response):
    assert get_request_returns_response.status_code == 200

def test_get_check_content_type_equals_json(get_request_returns_response):
    assert get_request_returns_response.headers['Content-Type'] == "application/json; charset=UTF-8"

# @pytest.mark.parametrize("index,id", [(0, "1859"), (1, "1863"), (2, "1864")])
# def test_get_payload(index, id, get_convert_response_to_json):    
#     assert get_convert_response_to_json["result"][index]["id"] == id

def test_get_results_return_twenty(get_convert_response_to_json):
     assert len(get_convert_response_to_json["result"]) == 20

####POST######################################################################################################################################################
POST_FIRST_NAME = "Connor"
POST_LAST_NAME = "Mote"
POST_GENDER = "male"

def test_get_check_status_code_equals_200(post_request_returns_response, post_get_convert_response_to_json):
    assert post_request_returns_response.status_code == 200
    assert post_get_convert_response_to_json["_meta"]["code"] == 200 #need to flip 

def test_post_check_content_type_equals_json(post_request_returns_response):
    assert post_request_returns_response.headers['Content-Type'] == "application/json; charset=UTF-8"

@pytest.mark.parametrize("key,value", [ ('first_name', POST_FIRST_NAME), ('last_name', POST_LAST_NAME),
                        ('gender', POST_GENDER)]) #put constants in sererate file
def test_get_payload(key, value, post_get_convert_response_to_json):         
    assert post_get_convert_response_to_json["result"]["id"] != None
    assert post_get_convert_response_to_json["result"][key] == value

###PUT#######################################################################################################################################################
# PUT_FIRST_NAME = "Connor"
# PUT_ID = "1859"
# payload = {
#     "first_name":PUT_FIRST_NAME
# }

# @pytest.fixture(scope="module")
# def put_request_returns_response():    
#     response = requests.put("https://gorest.co.in/public-api/users/" + PUT_ID, headers={'Authorization': 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'}, data = payload)        
#     return response

# @pytest.fixture(scope="module") #put fixtures into one file
# def put_get_convert_response_to_json(put_request_returns_response):    
#     response_body = put_request_returns_response.json()
#     return response_body

# def test_get_check_status_code_equals_200(put_request_returns_response, put_get_convert_response_to_json):
#     assert put_request_returns_response.status_code == 200
#     assert put_get_convert_response_to_json["_meta"]["code"] == 200

# def test_put_check_content_type_equals_json(put_request_returns_response):
#     assert put_request_returns_response.headers['Content-Type'] == "application/json; charset=UTF-8"

# @pytest.mark.parametrize("key,value", [ ('id', PUT_ID), ('first_name', PUT_FIRST_NAME), ('last_name', "Brandy")])
# def test_get_payload(key, value, put_get_convert_response_to_json):   
#     assert put_get_convert_response_to_json["result"][key] == value

# ##DELETE#####################################################################################################################################################
# DELETE_ID = "1883" #need to change every time or create a POST during tear down

# @pytest.fixture(scope="module")
# def delete_request_returns_response():    
#     response = requests.delete("https://gorest.co.in/public-api/users/" + DELETE_ID, headers={'Authorization': 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'})        
#     return response

# @pytest.fixture(scope="module")
# def delete_get_convert_response_to_json(delete_request_returns_response):    
#     response_body = delete_request_returns_response.json()
#     return response_body

# def test_get_check_status_code_equals_200(delete_request_returns_response, delete_get_convert_response_to_json):
#     assert delete_request_returns_response.status_code == 200
#     assert delete_get_convert_response_to_json["_meta"]["code"] == 204

# def test_delete_check_content_type_equals_json(delete_request_returns_response):
#     assert delete_request_returns_response.headers['Content-Type'] == "application/json; charset=UTF-8"

# def test_get_payload(delete_get_convert_response_to_json):   
#     assert delete_get_convert_response_to_json["result"] == None

# def test_basic():
#     print("hello")
#     assert 2 == 2