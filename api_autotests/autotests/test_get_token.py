from playwright.sync_api import APIRequestContext, expect
from ..requests_data.load_json import load_json
from ..rb_api import RestfulBookerAPI
from jsonschema import validate


def test_get_token(api_request_context: APIRequestContext):
    auth_data = load_json("requests_data/auth_data.json")
    valid_schema = load_json("requests_data/token_schema.json")
    rb = RestfulBookerAPI(api_request_context)

    response = rb.authorize(auth_data)

    validate(response.json(), valid_schema)
    expect(response).to_be_ok()
