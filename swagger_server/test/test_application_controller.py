# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.application import Application  # noqa: E501
from swagger_server.models.company import Company  # noqa: E501
from swagger_server.test import BaseTestCase


class TestApplicationController(BaseTestCase):
    """ApplicationController integration test stubs"""

    def test_application_post(self):
        """Test case for application_post

        add appplication
        """
        body = Application()
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/application',
            method='POST',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_deleteapplication(self):
        """Test case for deleteapplication

        Delete application
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/application/{id}'.format(id=1.2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getapplication_bycandidate_id(self):
        """Test case for getapplication_bycandidate_id

        Get application by candidate id
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/application/{candidateid}'.format(candidateid=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
