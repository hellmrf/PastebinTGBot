"""PasteBin API Class
Based on code by acidvegas

"""
# API Documentation: https://pastebin.com/api

import requests


class PasteBin:

    def __init__(self, api_dev_key, api_user_key=None, timeout=10):
        self.api_dev_key = api_dev_key
        self.api_user_key = api_user_key
        self.timeout = timeout

    def api_call(self, params, method="api_post.php"):
        url = 'https://pastebin.com/api/'+method
        response = requests.post(url, data=params, timeout=self.timeout)
        return response.text

    def create_user_key(self, username, password):
        params = {'api_dev_key': self.api_dev_key,
                  'api_user_name': username, 'api_user_password': password}
        return self.api_call('api_login.php', params)

    def paste(self, data, guest=True, name=None, format=None, private=None, expire=None):
        params = {'api_dev_key': self.api_dev_key,
                  'api_option': 'paste', 'api_paste_code': data}
        if not guest:
            params['api_user_key'] = self.api_user_key
        if name:
            params['api_paste_name'] = name
        if format:
            params['api_paste_format'] = format
        if private:
            params['api_paste_private'] = private
        if expire:
            params['api_paste_expire_date'] = expire
        return self.api_call(params)

    def list_pastes(self, results_limit=None):
        params = {'api_dev_key': self.api_dev_key,
                  'api_user_key': self.api_user_key, 'api_option': 'list'}
        if results_limit:  # Default 50, Minimum 1, Maximum 1000
            params['api_results_limit'] = results_limit
        return self.api_call(params)

    def trending_pastes(self):
        params = {'api_dev_key': self.api_dev_key, 'api_option': 'trends'}
        return self.api_call(params)

    def delete_paste(self, paste_key):
        params = {'api_dev_key': self.api_dev_key, 'api_user_key': self.api_user_key,
                  'api_paste_key': paste_key, 'api_option': 'delete'}
        return self.api_call(params)

    def user_info(self):
        params = {'api_dev_key': self.api_dev_key,
                  'api_user_key': self.api_user_key, 'api_option': 'userdetails'}
        return self.api_call(params)

    def raw_pastes(self, paste_key):
        params = {'api_dev_key': self.api_dev_key, 'api_user_key': self.api_user_key,
                  'api_paste_key': paste_key, 'api_option': 'show_paste'}
        return self.api_call(params, 'api_raw.php')
