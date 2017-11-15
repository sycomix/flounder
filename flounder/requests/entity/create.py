# -*- coding:utf8 -*-
# !/usr/bin/env python

from ..request import Request


class CreateRequest(Request):
    """
        Abstract request class
        Contain share information for all query requests.
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

    def __init__(self, client_access_token, base_url, version):
        super(CreateRequest, self).__init__(client_access_token, base_url,
                                            '/v1/entities', {
                                                'v': version
                                            })

        self.lang = 'en'
        self.entities = None
        self.version = version

    def _prepare_entities(self):
        if self.entities:
            return list(map(lambda x: x._to_dict(), self.entities))
        return None
