import requests
import pytest
import json

#happy paths
####GET#####################################################################################################################################################
@pytest.mark.gethappy
class TestGetHappy:
    def test_get_check_status_code_equals_200(self, get_request_returns_response):
        assert get_request_returns_response.status_code == 200

    def test_get_check_content_type_equals_json(self, get_request_returns_response):
        assert get_request_returns_response.headers['Content-Type'] == "application/json; charset=UTF-8"

    def test_get_results_return_twenty(self, get_convert_response_to_json):
        assert len(get_convert_response_to_json["result"]) == 20

# ####POST######################################################################################################################################################
POST_FIRST_NAME = "Connor"
POST_LAST_NAME = "Mote"
POST_GENDER = "male"

@pytest.mark.posthappy
class TestPostHappy:
    def test_get_check_status_code_equals_200(self, post_request_returns_response, post_get_convert_response_to_json):
        assert post_request_returns_response.status_code == 200
        assert post_get_convert_response_to_json["_meta"]["code"] == 200 #need to flip 

    def test_post_check_content_type_equals_json(self, post_request_returns_response):
        assert post_request_returns_response.headers['Content-Type'] == "application/json; charset=UTF-8"

    @pytest.mark.parametrize("key,value", [ ('first_name', POST_FIRST_NAME), ('last_name', POST_LAST_NAME),
                            ('gender', POST_GENDER)]) #put constants in sererate file
    def test_get_payload(self, key, value, post_get_convert_response_to_json):         
        assert post_get_convert_response_to_json["result"]["id"] != None
        assert post_get_convert_response_to_json["result"][key] == value

###PUT#######################################################################################################################################################

@pytest.mark.puthappy
class TestPutHappy:
    def test_get_check_status_code_equals_200(self, put_request_returns_response, put_get_convert_response_to_json):
        assert put_request_returns_response.status_code == 200 #need to flip
        assert put_get_convert_response_to_json["_meta"]["code"] == 200

    def test_put_check_content_type_equals_json(self, put_request_returns_response):
        x =  put_request_returns_response.headers['Content-Type']
        assert x == "application/json; charset=UTF-8"
        y = 1

    def test_get_payload(self, put_get_convert_response_to_json, return_PutData_obj):   
        assert put_get_convert_response_to_json["result"]['id'] == return_PutData_obj.ID
        assert put_get_convert_response_to_json["result"]['first_name'] == return_PutData_obj.PUT_FIRST_NAME

# ##DELETE#####################################################################################################################################################
@pytest.mark.deletehappy
class TestDeleteHappy:
    def test_get_check_status_code_equals_200(self, delete_request_returns_response, delete_get_convert_response_to_json):
        assert delete_request_returns_response.status_code == 200
        assert delete_get_convert_response_to_json["_meta"]["code"] == 204

    def test_delete_check_content_type_equals_json(self, delete_request_returns_response):
        assert delete_request_returns_response.headers['Content-Type'] == "application/json; charset=UTF-8"

    def test_get_payload(self, delete_get_convert_response_to_json):   
        assert delete_get_convert_response_to_json["result"] == None
