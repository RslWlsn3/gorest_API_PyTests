import pytest

EXPECTED_CONTENT_TYPE = "application/json; charset=UTF-8"

# ###GET###################################################################
# happy paths


@pytest.mark.get
class TestGet:
    def test_GET_check_status_code_equals_200(
            self, GET_request_returns_response):
        assert 200 == GET_request_returns_response.status_code

    def test_GET_check_content_type_equals_json(
            self, GET_request_returns_response):
        assert (EXPECTED_CONTENT_TYPE ==
                GET_request_returns_response.headers['Content-Type'])

    def test_GET_results_return_twenty(self, GET_convert_response_to_json):
        assert 20 == len(GET_convert_response_to_json["result"])

# Negative testing
    def test_GET_check_status_code_equals_404(
            self, GET_fake_id):
        assert 200 == GET_fake_id.status_code
        response_body = GET_fake_id.json()
        assert 404 == response_body["_meta"]["code"]
        assert 404 == response_body["result"]["status"]

    def test_GET_bad_authorization_401(self, GET_bad_authorization_code):
        assert 200 == GET_bad_authorization_code.status_code
        response_body = GET_bad_authorization_code.json()
        assert 401 == response_body["_meta"]["code"]

    # I need to raise the exception in my own code to be able to catch it
    # def test_GET_bad_url_404(self):
    #     with pytest.raises(ConnectionError):
    #         requests.get(
    #             "https://gorasdfest.co.in/public-api/users",
    #             headers={'Authorization':
    #                 'Bearer VqRUbB84gJ6bMP97UeRK3MYpC608ZRcsVVYd'})


# ####POST#################################################################
POST_FIRST_NAME = "Connor"
POST_LAST_NAME = "Mote"
POST_GENDER = "male"


@pytest.mark.post
class TestPost:
    def test_POST_check_status_code_equals_200(
            self,
            POST_request_returns_response,
            POST_convert_response_to_json):
        assert 200 == POST_request_returns_response.status_code
        assert 200 == POST_convert_response_to_json["_meta"]["code"]

    def test_POST_check_content_type_equals_json(
            self, POST_request_returns_response):
        assert (EXPECTED_CONTENT_TYPE ==
                POST_request_returns_response.headers['Content-Type'])

    @pytest.mark.parametrize("key,value",
                             [('first_name',
                               POST_FIRST_NAME),
                              ('last_name',
                               POST_LAST_NAME),
                                 ('gender',
                                  POST_GENDER)])  # consts in separate file
    def test_POST_payload(self, key, value, POST_convert_response_to_json):
        assert None is not POST_convert_response_to_json["result"]["id"]
        assert value == POST_convert_response_to_json["result"][key]

# Negative testing
    def test_check_status_code_equals_422(
            self,
            negative_POST_request_returns_response,
            negative_POST_request_returns_json):
        assert 200 == negative_POST_request_returns_response.status_code
        assert 422 == negative_POST_request_returns_json["_meta"]["code"]
# ##PUT####################################################################


@pytest.mark.put
class TestPut:
    def test_PUT_check_status_code_equals_200(
            self,
            PUT_request_returns_response,
            PUT_convert_response_to_json):
        assert 200 == PUT_request_returns_response.status_code
        assert 200 == PUT_convert_response_to_json["_meta"]["code"]

    def test_PUT_check_content_type_equals_json(
            self, PUT_request_returns_response):
        content_type = PUT_request_returns_response.headers['Content-Type']
        assert EXPECTED_CONTENT_TYPE == content_type

    def test_PUT_payload(
            self,
            PUT_convert_response_to_json,
            return_PUTData_obj):
        assert (return_PUTData_obj.ID ==
                PUT_convert_response_to_json["result"]['id'])
        assert (return_PUTData_obj.PUT_FIRST_NAME ==
                PUT_convert_response_to_json["result"]['first_name'])

# Negative testing
    def test_check_status_code_equals_404(
            self,
            negative_PUT_request_returns_response,
            negative_PUT_convert_response_to_json):
        assert 200 == negative_PUT_request_returns_response.status_code
        assert 404 == negative_PUT_convert_response_to_json["_meta"]["code"]

# ##DELETE#################################################################


@pytest.mark.delete
class TestDelete:
    def test_DELETE_check_status_code_equals_200(
            self,
            DELETE_request_returns_response,
            DELETE_convert_response_to_json):
        assert 200 == DELETE_request_returns_response.status_code
        assert 204 == DELETE_convert_response_to_json["_meta"]["code"]

    def test_DELETE_check_content_type_equals_json(
            self, DELETE_request_returns_response):
        assert (EXPECTED_CONTENT_TYPE ==
                DELETE_request_returns_response.headers['Content-Type'])

    def test_DELETE_payload(self, DELETE_convert_response_to_json):
        assert None is DELETE_convert_response_to_json["result"]

# Negative testing
    def test_GET_check_status_code_equals_404(
            self,
            negative_DELETE_request_returns_response,
            negative_DELETE_convert_response_to_json):
        assert 200 == negative_DELETE_request_returns_response.status_code
        assert 404 == negative_DELETE_convert_response_to_json["_meta"]["code"]
