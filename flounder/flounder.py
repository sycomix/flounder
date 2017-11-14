# -*- coding:utf8 -*-
# !/usr/bin/env python

class Flounder(object):

    @property
    def client_access_token(self):
        """
            Client access token provided by https://dialogflow.com/
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