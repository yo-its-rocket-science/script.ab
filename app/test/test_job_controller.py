# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.job import Job  # noqa: E501
from app.test import BaseTestCase


class TestJobController(BaseTestCase):
    """JobController integration test stubs"""

    def test_delete_job(self):
        """Test case for delete_job

        Delete job
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/job/{id}'.format(id=1.2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_job_by_id(self):
        """Test case for get_job_by_id

        get job by id
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/job/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_job_post(self):
        """Test case for job_post

        add job
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/job',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_putjob(self):
        """Test case for putjob


        """
        body = Job()
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/job/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
