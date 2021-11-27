# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.skill import Skill  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSkillController(BaseTestCase):
    """SkillController integration test stubs"""

    def test_skill_get(self):
        """Test case for skill_get

        get list of skills for company to select
        """
        response = self.client.open(
            '/rocketscience/ScriptAB/1.0.0/skill',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
