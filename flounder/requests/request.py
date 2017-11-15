# -*- coding:utf8 -*-
# !/usr/bin/env python

import urllib
import os

try:  # Python 3
    from http.client import HTTPSConnection
except ImportError:
    from httplib import HTTPSConnection

try:
    import urllib.parse
except ImportError:
    import urllib


class Request(object):
    """Abstract request class
    Contain share information for all requests."""

    _connection_class = HTTPSConnection

    @property
    def client_access_token(self):
        """client access token provided by http://api.ai/"""
        return self._client_access_token

    @client_access_token.setter
    def client_access_token(self, client_access_token):
        self._client_access_token = client_access_token

    def __init__(self,
                 client_access_token,
                 base_url,
                 path,
                 query_parameters=[]):
        super(Request, self).__init__()

        self.base_url = base_url
        self.path = path
        self.query_parameters = query_parameters

        self.client_access_token = client_access_token

        self._prepare_proxy()
        self._prepare_request()

    def _prepare_entities(self):
        if self.entities:
            return list(map(lambda x: x._to_dict(), self.entities))
        return None

    def _prepare_proxy(self):

        self.proxy_enabled = False

        if os.environ.get("https_proxy"):
            self.proxy_enabled = True
            https_proxy = os.environ["https_proxy"]

            # As proxies are set like "export https_proxy=$http_proxy"
            # so it might start with 'https' or 'http'

            https_proxy = https_proxy.replace("https://", "").rstrip("/")
            https_proxy = https_proxy.replace("http://", "").rstrip("/")
            (self.proxy_host, self.proxy_port) = https_proxy.split(":")
            self.proxy_port = int(self.proxy_port)

    def _prepare_request(self, debug=False):
        if (self.proxy_enabled):
            self._connection = self._connection_class(self.proxy_host,
                                                      self.proxy_port)

            self._connection.set_tunnel(self.base_url)
        else:
            self._connection = self._connection_class(self.base_url)

    def _connect(self):
        self._connection.connect()

        query = None

        try:
            query = urllib.urlencode(self.query_parameters)
        except AttributeError:
            query = urllib.parse.urlencode(self.query_parameters)

        full_path = self.path + '?' + query

        self._connection.putrequest('POST', full_path, skip_accept_encoding=1)

        headers = {
            'Accept': 'application/json',
            'Authorization': ('Bearer %s' % self.client_access_token)
        }

        headers.update(headers)

        for header_key, header_value in headers.items():
            self._connection.putheader(header_key, header_value)

        self._connection.endheaders()

    def getresponse(self):
        """Send all data and wait for response.
        """
        self._connect()
        print self.__dict__.keys()
        return self._connection.getresponse()