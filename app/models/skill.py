from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app import util


class Skill(Model):
    def __init__(self, id: int = None, name: str = None):  # noqa: E501
        """Skill - a model defined in Swagger

        :param id: The id of this Skill.  # noqa: E501
        :type id: int
        :param name: The name of this Skill.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }
        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Skill':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Skill of this Skill.  # noqa: E501
        :rtype: Skill
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Skill.


        :return: The id of this Skill.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Skill.


        :param id: The id of this Skill.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Skill.


        :return: The name of this Skill.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Skill.


        :param name: The name of this Skill.
        :type name: str
        """

        self._name = name
