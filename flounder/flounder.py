# -*- coding:utf8 -*-
# !/usr/bin/env python


from .requests import CreateRequest

DEFAULT_VERSION = '20150910'


class Flounder(object):
    """
        Create entities
    """
    @property
    def client_access_token(self):
        """
            :rtype: str or unicode
        """

        return self._client_access_token

    @client_access_token.setter
    def client_access_token(self, client_access_token):
        """
            :type client_access_token: str or unicode
        """

        self._client_access_token = client_access_token

    def __init__(self, client_access_token):
        super(Flounder, self).__init__()
        self._client_access_token = client_access_token

        self._base_url = 'api.dialogflow.com'
        self._version = DEFAULT_VERSION

    def create_request(self):
        """
            (session_id, version,client_access_token).
            :rtype TextRequest:
        """

        request = CreateRequest(
            self.client_access_token,
            self._base_url,
            self._version,
        )
        return request
