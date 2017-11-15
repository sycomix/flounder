# -*- coding:utf8 -*-
# !/usr/bin/env python

import json

from ..request import Request

from time import gmtime
from time import strftime

class CreateRequest(Request):
    """
        Abstract request class
        Contain share information for all Create requests.
    """

    @property
    def entities(self):
        """Array of entities that replace developer defined entities for this
        request only.
        The entity(ies) need to exist in the developer console."""
        return self._entities

    @entities.setter
    def entities(self, entities):
        self._entities = entities

    def __init__(self, client_access_token, base_url, version,entities=[]):
        super(CreateRequest, self).__init__(client_access_token,
                                           base_url,
                                           '/v1/entities',
                                           {'v': version}
                                           )
        self._entities = entities
        self.version = version

    def _prepare_headers(self):
        return {
            'Content-Type': 'application/json;',
            'Authorization': ('Bearer %s' % self.client_access_token)
        }

    def _prepage_begin_request_data(self):
        return None

    def _prepage_end_request_data(self):
        return None