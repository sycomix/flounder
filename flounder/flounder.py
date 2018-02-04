# -*- coding:utf8 -*-
# !/usr/bin/env python

try:  # Python 3
    from http.client import HTTPSConnection
except ImportError:
    from httplib import HTTPSConnection

import csv
import uuid
import warnings

from .requests.entity.create import CreateRequest
from text_utility import to_romaji
from text_utility import to_hiragana
from text_utility import to_katakana


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

    def __init__(self,
                 client_access_token,
                 entity_name=None,
                 entity_csv=None,
                 session_id=None):
        super(Flounder, self).__init__()
        self._client_access_token = client_access_token
        self._base_url = 'api.dialogflow.com'
        self._version = DEFAULT_VERSION

        if session_id is None:
            self._session_id = uuid.uuid4().hex
        else:
            self._session_id = session_id

    def create_request(self, entity_name, csv_path):
        entity = self.create_entity(entity_name, csv_path)
        request = CreateRequest(self.client_access_token, self._base_url,
                                self._version, entity)
        return request

    def create_entity(self, name, csv_path):
        synonyms = self.to_list(csv_path)
        tmp_list = []
        for synonym in synonyms:
            romaji = to_romaji(synonym)
            hiragana = to_hiragana(synonym)
            katakana = to_katakana(synonym)
            new_synonym = {
                "synonyms": [synonym, romaji, hiragana, katakana],
                "value": romaji
            }
            tmp_list.append(new_synonym)
        return {"entries": tmp_list, "name": name}

    def to_list(self, csv_path):
        tmp_list = []
        with open(csv_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                tmp_list.append(row[0])
            return tmp_list
