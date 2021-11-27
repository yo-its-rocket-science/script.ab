# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from app.models.candidate import Candidate  # noqa: E501
from app.test import BaseTestCase


class TestCandidateController(BaseTestCase):
    """CandidateController integration test stubs"""

    def test_delete_candidate(self):
        """Test case for delete_candidate

        Delete user
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/candidate/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_candidate_by_id(self):
        """Test case for get_candidate_by_id

        get candidate by their id
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/candidate/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_candidate(self):
        """Test case for update_candidate

        Updated candidate
        """
        body = Candidate()
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/candidate/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='*/*')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
