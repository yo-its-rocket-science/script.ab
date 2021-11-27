# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCompanyController(BaseTestCase):
    """CompanyController integration test stubs"""

    def test_add_company(self):
        """Test case for add_company

        add company
        """
        body = Company()
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/company',
            method='POST',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_company(self):
        """Test case for delete_company

        
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/company/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_company_by_id(self):
        """Test case for get_company_by_id

        Get candidate by id
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/company/{id}'.format(id=1.2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_company(self):
        """Test case for put_company

        
        """
        body = Company()
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/company/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
