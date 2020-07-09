import pytest


# happy paths
# ###GET###################################################################
@pytest.mark.gethappy
class TestGetHappy:
    def test_get_check_status_code_equals_200(
            self, get_request_returns_response):
        assert 200 == get_request_returns_response.status_code

    def test_get_check_content_type_equals_json(
            self, get_request_returns_response):
        assert ("application/json; charset=UTF-8" ==
                get_request_returns_response.headers['Content-Type'])

    def test_get_results_return_twenty(self, get_convert_response_to_json):
        assert 20 == len(get_convert_response_to_json["result"])


# ####POST#################################################################
POST_FIRST_NAME = "Connor"
POST_LAST_NAME = "Mote"
POST_GENDER = "male"


@pytest.mark.posthappy
class TestPostHappy:
    def test_get_check_status_code_equals_200(
            self,
            post_request_returns_response,
            post_get_convert_response_to_json):
        assert 200 == post_request_returns_response.status_code
        assert 200 == post_get_convert_response_to_json["_meta"]["code"]

    def test_post_check_content_type_equals_json(
            self, post_request_returns_response):
        assert ("application/json; charset=UTF-8" ==
                post_request_returns_response.headers['Content-Type'])

    @pytest.mark.parametrize("key,value",
                             [('first_name',
                               POST_FIRST_NAME),
                              ('last_name',
                               POST_LAST_NAME),
                                 ('gender',
                                  POST_GENDER)])  # consts in separate file
    def test_get_payload(self, key, value, post_get_convert_response_to_json):
        assert None is not post_get_convert_response_to_json["result"]["id"]
        assert value == post_get_convert_response_to_json["result"][key]

# ##PUT####################################################################


@pytest.mark.puthappy
class TestPutHappy:
    def test_get_check_status_code_equals_200(
            self,
            put_request_returns_response,
            put_get_convert_response_to_json):
        assert 200 == put_request_returns_response.status_code
        assert 200 == put_get_convert_response_to_json["_meta"]["code"]

    def test_put_check_content_type_equals_json(
            self, put_request_returns_response):
        content_type = put_request_returns_response.headers['Content-Type']
        assert "application/json; charset=UTF-8" == content_type

    def test_get_payload(
            self,
            put_get_convert_response_to_json,
            return_PutData_obj):
        assert (return_PutData_obj.ID ==
                put_get_convert_response_to_json["result"]['id'])
        assert (return_PutData_obj.PUT_FIRST_NAME ==
                put_get_convert_response_to_json["result"]['first_name'])

# ##DELETE#################################################################


@pytest.mark.deletehappy
class TestDeleteHappy:
    def test_get_check_status_code_equals_200(
            self,
            delete_request_returns_response,
            delete_get_convert_response_to_json):
        assert 200 == delete_request_returns_response.status_code
        assert 204 == delete_get_convert_response_to_json["_meta"]["code"]

    def test_delete_check_content_type_equals_json(
            self, delete_request_returns_response):
        assert ("application/json; charset=UTF-8" ==
                delete_request_returns_response.headers['Content-Type'])

    def test_get_payload(self, delete_get_convert_response_to_json):
        assert None is delete_get_convert_response_to_json["result"]
