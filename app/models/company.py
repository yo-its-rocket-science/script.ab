from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.job import Job  # noqa: F401,E501
from app import util


class Company(Model):

    def __init__(self, id: int = None, userid: int = None, name: str = None, size: str = None, type: str = None, image: str = None, jobs: List[Job] = None):  # noqa: E501
        """Company - a model defined in Swagger

        :param id: The id of this Company.  # noqa: E501
        :type id: int
        :param userid: The userid of this Company.  # noqa: E501
        :type userid: int
        :param name: The name of this Company.  # noqa: E501
        :type name: str
        :param size: The size of this Company.  # noqa: E501
        :type size: str
        :param type: The type of this Company.  # noqa: E501
        :type type: str
        :param image: The image of this Company.  # noqa: E501
        :type image: str
        :param jobs: The jobs of this Company.  # noqa: E501
        :type jobs: List[Job]
        """
        self.swagger_types = {
            'id': int,
            'userid': int,
            'name': str,
            'size': str,
            'type': str,
            'image': str,
            'jobs': List[Job]
        }

        self.attribute_map = {
            'id': 'id',
            'userid': 'userid',
            'name': 'name',
            'size': 'size',
            'type': 'type',
            'image': 'image',
            'jobs': 'jobs'
        }
        self._id = id
        self._userid = userid
        self._name = name
        self._size = size
        self._type = type
        self._image = image
        self._jobs = jobs

    @classmethod
    def from_dict(cls, dikt) -> 'Company':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Company of this Company.  # noqa: E501
        :rtype: Company
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Company.


        :return: The id of this Company.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Company.


        :param id: The id of this Company.
        :type id: int
        """

        self._id = id

    @property
    def userid(self) -> int:
        """Gets the userid of this Company.


        :return: The userid of this Company.
        :rtype: int
        """
        return self._userid

    @userid.setter
    def userid(self, userid: int):
        """Sets the userid of this Company.


        :param userid: The userid of this Company.
        :type userid: int
        """

        self._userid = userid

    @property
    def name(self) -> str:
        """Gets the name of this Company.


        :return: The name of this Company.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Company.


        :param name: The name of this Company.
        :type name: str
        """

        self._name = name

    @property
    def size(self) -> str:
        """Gets the size of this Company.


        :return: The size of this Company.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size: str):
        """Sets the size of this Company.


        :param size: The size of this Company.
        :type size: str
        """

        self._size = size

    @property
    def type(self) -> str:
        """Gets the type of this Company.


        :return: The type of this Company.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Company.


        :param type: The type of this Company.
        :type type: str
        """

        self._type = type

    @property
    def image(self) -> str:
        """Gets the image of this Company.


        :return: The image of this Company.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this Company.


        :param image: The image of this Company.
        :type image: str
        """

        self._image = image

    @property
    def jobs(self) -> List[Job]:
        """Gets the jobs of this Company.


        :return: The jobs of this Company.
        :rtype: List[Job]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs: List[Job]):
        """Sets the jobs of this Company.


        :param jobs: The jobs of this Company.
        :type jobs: List[Job]
        """

        self._jobs = jobs
