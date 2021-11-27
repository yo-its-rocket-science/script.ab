from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app import util


class Application(Model):
    def __init__(self, id: int = None, jobid: int = None, candidateid: int = None, companyid: int = None):  # noqa: E501
        """Application - a model defined in Swagger

        :param id: The id of this Application.  # noqa: E501
        :type id: int
        :param jobid: The jobid of this Application.  # noqa: E501
        :type jobid: int
        :param candidateid: The candidateid of this Application.  # noqa: E501
        :type candidateid: int
        :param companyid: The companyid of this Application.  # noqa: E501
        :type companyid: int
        """
        self.swagger_types = {
            'id': int,
            'jobid': int,
            'candidateid': int,
            'companyid': int
        }

        self.attribute_map = {
            'id': 'id',
            'jobid': 'jobid',
            'candidateid': 'candidateid',
            'companyid': 'companyid'
        }
        self._id = id
        self._jobid = jobid
        self._candidateid = candidateid
        self._companyid = companyid

    @classmethod
    def from_dict(cls, dikt) -> 'Application':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Application of this Application.  # noqa: E501
        :rtype: Application
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Application.


        :return: The id of this Application.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Application.


        :param id: The id of this Application.
        :type id: int
        """

        self._id = id

    @property
    def jobid(self) -> int:
        """Gets the jobid of this Application.


        :return: The jobid of this Application.
        :rtype: int
        """
        return self._jobid

    @jobid.setter
    def jobid(self, jobid: int):
        """Sets the jobid of this Application.


        :param jobid: The jobid of this Application.
        :type jobid: int
        """

        self._jobid = jobid

    @property
    def candidateid(self) -> int:
        """Gets the candidateid of this Application.


        :return: The candidateid of this Application.
        :rtype: int
        """
        return self._candidateid

    @candidateid.setter
    def candidateid(self, candidateid: int):
        """Sets the candidateid of this Application.


        :param candidateid: The candidateid of this Application.
        :type candidateid: int
        """

        self._candidateid = candidateid

    @property
    def companyid(self) -> int:
        """Gets the companyid of this Application.


        :return: The companyid of this Application.
        :rtype: int
        """
        return self._companyid

    @companyid.setter
    def companyid(self, companyid: int):
        """Sets the companyid of this Application.


        :param companyid: The companyid of this Application.
        :type companyid: int
        """

        self._companyid = companyid
