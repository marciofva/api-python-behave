import json
import os
from http import HTTPStatus
import requests
from hamcrest import equal_to, assert_that
from services.helpers.utils import get_header_json, print_logs, get_base_header


class Rest_Service:

    _author_path = "/v1/Authors/"

    def get_token(self, context):
        auth_data = {
            "client_id": "abcd",
            "client_secret": "eio"
        }
        response = requests.post(url=context.credentials["AUTH"], data=auth_data, headers=get_base_header())
        assert_that(response.status_code, equal_to(HTTPStatus.OK), "Token Authorization")
        return (json.loads(response.text))["access_token"]

    def get_author(self, context):
        path = context.credentials["HOST"] + self._author_path

        response = requests.get(url=path+context.author_id, headers=get_header_json())
        print_logs(response, context)
        return response

    def create_author(self, context):
        path = context.credentials["HOST"] + self._author_path

        response = requests.post(url=path, json=context.payload, headers=get_header_json())
        print_logs(response, context)
        return response

    def get_author_with_auth(self, context):
        path = context.credentials["HOST"] + self._author_path

        params = {'field1': 'ab',
                  'field2': 'cd'}
        headers = {"Authorization":  context.token}

        response = requests.get(url=path, params=params, headers=headers)
        return response

    def upload_file(self, context):
        path = context.credentials["HOST"] + "/file?id={}"

        headers = {'Accept': '*/*', 'User-Agent': 'request'}

        document_file = "bexs.jpeg"

        # Set document path
        path = os.getcwd() + "/upload/" + document_file

        # Set files parameter
        content_type = "image/jpeg"
        files = [('file', (document_file, open(path, 'rb'), content_type))]

        # Post the request
        response = requests.post(url=path.format(123), headers=headers, files=files)
