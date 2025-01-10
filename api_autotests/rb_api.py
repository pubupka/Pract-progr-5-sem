from playwright.sync_api import APIRequestContext

class RestfulBookerAPI:
    def __init__(self, api_request_context: APIRequestContext):
        self.url = "https://restful-booker.herokuapp.com"
        self.api_request_context = api_request_context

    def create_booking(self, new_booking_data):
        url = f"{self.url}/booking"
        response = self.api_request_context.post(url, data=new_booking_data)
        return response

    def authorize(self, auth_data):
            url = f"{self.url}/auth"
            response = self.api_request_context.post(url, data=auth_data)
            return response

    def delete_booking(self, booking_id, token):
        url = f"{self.url}/booking/{booking_id}"
        headers = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        response = self.api_request_context.delete(url, headers=headers)
        return response
