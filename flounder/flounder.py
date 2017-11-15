# -*- coding:utf8 -*-
# !/usr/bin/env python

try:  # Python 3
    from http.client import HTTPSConnection
except ImportError:
    from httplib import HTTPSConnection

import uuid

from .requests import (
    CreateRequest
)

import warnings

DEFAULT_VERSION = '20150910'


class Flounder(object):
    _connection_class = HTTPSConnection

    @property
    def client_access_token(self):
        """
            Client access token provided by https://daialogflow.com/

            :rtype: str or unicode
        """

        return self._client_access_token

    @client_access_token.setter
    def client_access_token(self, client_access_token):
        """
            :type client_access_token: str or unicode
        """

        self._client_access_token = client_access_token

    @property
    def entities(self):
        return self._entities

    @entities.setter
    def entities(self, entities=[]):
        self._entities = entities

    def __init__(self, client_access_token, session_id=None):
        super(Flounder, self).__init__()
        self._client_access_token = client_access_token
        self._entities = []
        self._base_url = 'api.dialogflow.com'
        self._version = DEFAULT_VERSION

        if session_id is None:
            self._session_id = uuid.uuid4().hex
        else:
            self._session_id = session_id


    def create_request(self):
        request = CreateRequest(
            self.client_access_token,
            self._base_url,
            self._version,
            self.entities
        )

        return request
