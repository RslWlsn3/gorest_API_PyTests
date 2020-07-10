import pytest


# ###GET###################################################################
# happy paths
@pytest.mark.get
class TestGet:
    def test_get_check_status_code_equals_200(
            self, get_request_returns_response):
        assert 200 == get_request_returns_response.status_code

    def test_get_check_content_type_equals_json(
            self, get_request_returns_response):
        assert ("application/json; charset=UTF-8" ==
                get_request_returns_response.headers['Content-Type'])

    def test_get_results_return_twenty(self, get_convert_response_to_json):
        assert 20 == len(get_convert_response_to_json["result"])

# Negative testing
    def test_get_check_status_code_equals_404(
            self, get_bad_request):
        assert 200 == get_bad_request.status_code
        response_body = get_bad_request.json()
        assert 404 == response_body["_meta"]["code"]
        assert 404 == response_body["result"]["status"]


# ####POST#################################################################
POST_FIRST_NAME = "Connor"
POST_LAST_NAME = "Mote"
POST_GENDER = "male"


@pytest.mark.post
class TestPost:
    def test_check_status_code_equals_200(
            self,
            post_request_returns_response,
            post_convert_response_to_json):
        assert 200 == post_request_returns_response.status_code
        assert 200 == post_convert_response_to_json["_meta"]["code"]

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
    def test_post_payload(self, key, value, post_convert_response_to_json):
        assert None is not post_convert_response_to_json["result"]["id"]
        assert value == post_convert_response_to_json["result"][key]

# Negative testing
    def test_check_status_code_equals_422(
            self,
            negative_post_request_returns_response,
            negative_post_request_returns_json):
        assert 200 == negative_post_request_returns_response.status_code
        assert 422 == negative_post_request_returns_json["_meta"]["code"]
# ##PUT####################################################################


@pytest.mark.put
class TestPut:
    def test_check_status_code_equals_200(
            self,
            put_request_returns_response,
            put_convert_response_to_json):
        assert 200 == put_request_returns_response.status_code
        assert 200 == put_convert_response_to_json["_meta"]["code"]

    def test_put_check_content_type_equals_json(
            self, put_request_returns_response):
        content_type = put_request_returns_response.headers['Content-Type']
        assert "application/json; charset=UTF-8" == content_type

    def test_put_payload(
            self,
            put_convert_response_to_json,
            return_PutData_obj):
        assert (return_PutData_obj.ID ==
                put_convert_response_to_json["result"]['id'])
        assert (return_PutData_obj.PUT_FIRST_NAME ==
                put_convert_response_to_json["result"]['first_name'])

# Negative testing
    def test_check_status_code_equals_404(
            self,
            negative_put_request_returns_response,
            negative_put_convert_response_to_json):
        assert 200 == negative_put_request_returns_response.status_code
        assert 404 == negative_put_convert_response_to_json["_meta"]["code"]

# ##DELETE#################################################################


@pytest.mark.delete
class TestDelete:
    def test_check_status_code_equals_200(
            self,
            delete_request_returns_response,
            delete_convert_response_to_json):
        assert 200 == delete_request_returns_response.status_code
        assert 204 == delete_convert_response_to_json["_meta"]["code"]

    def test_delete_check_content_type_equals_json(
            self, delete_request_returns_response):
        assert ("application/json; charset=UTF-8" ==
                delete_request_returns_response.headers['Content-Type'])

    def test_delete_payload(self, delete_convert_response_to_json):
        assert None is delete_convert_response_to_json["result"]

# Negative testing
    def test_get_check_status_code_equals_404(
            self,
            negative_delete_request_returns_response,
            negative_delete_convert_response_to_json):
        assert 200 == negative_delete_request_returns_response.status_code
        assert 404 == negative_delete_convert_response_to_json["_meta"]["code"]
