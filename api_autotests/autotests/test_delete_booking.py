from playwright.sync_api import APIRequestContext, expect
from ..requests_data.load_json import load_json
from ..rb_api import RestfulBookerAPI


def test_delete_booking(api_request_context: APIRequestContext):
    auth_data = load_json("requests_data/auth_data.json")
    new_booking_data = load_json("requests_data/new_booking_data.json")
    rb = RestfulBookerAPI(api_request_context)

    id = rb.create_booking(new_booking_data).json()["bookingid"]
    token = rb.authorize(auth_data).json()["token"]

    response = rb.delete_booking(id, token)

    expect(response).to_be_ok()
    