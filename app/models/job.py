from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.skill import Skill  # noqa: F401,E501
from app import util


class Job(Model):
    def __init__(self, id: int = None, company_id: int = None, title: str = None, description: str = None, workplace_type: str = None, employment_type: str = None, salary: str = None, skills: List[Skill] = None):  # noqa: E501
        """Job - a model defined in Swagger

        :param id: The id of this Job.  # noqa: E501
        :type id: int
        :param company_id: The company_id of this Job.  # noqa: E501
        :type company_id: int
        :param title: The title of this Job.  # noqa: E501
        :type title: str
        :param description: The description of this Job.  # noqa: E501
        :type description: str
        :param workplace_type: The workplace_type of this Job.  # noqa: E501
        :type workplace_type: str
        :param employment_type: The employment_type of this Job.  # noqa: E501
        :type employment_type: str
        :param salary: The salary of this Job.  # noqa: E501
        :type salary: str
        :param skills: The skills of this Job.  # noqa: E501
        :type skills: List[Skill]
        """
        self.swagger_types = {
            'id': int,
            'company_id': int,
            'title': str,
            'description': str,
            'workplace_type': str,
            'employment_type': str,
            'salary': str,
            'skills': List[Skill]
        }

        self.attribute_map = {
            'id': 'id',
            'company_id': 'companyId',
            'title': 'title',
            'description': 'description',
            'workplace_type': 'workplaceType',
            'employment_type': 'employmentType',
            'salary': 'salary',
            'skills': 'skills'
        }
        self._id = id
        self._company_id = company_id
        self._title = title
        self._description = description
        self._workplace_type = workplace_type
        self._employment_type = employment_type
        self._salary = salary
        self._skills = skills

    @classmethod
    def from_dict(cls, dikt) -> 'Job':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Job of this Job.  # noqa: E501
        :rtype: Job
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Job.


        :return: The id of this Job.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Job.


        :param id: The id of this Job.
        :type id: int
        """

        self._id = id

    @property
    def company_id(self) -> int:
        """Gets the company_id of this Job.


        :return: The company_id of this Job.
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id: int):
        """Sets the company_id of this Job.


        :param company_id: The company_id of this Job.
        :type company_id: int
        """

        self._company_id = company_id

    @property
    def title(self) -> str:
        """Gets the title of this Job.


        :return: The title of this Job.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Job.


        :param title: The title of this Job.
        :type title: str
        """

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this Job.


        :return: The description of this Job.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Job.


        :param description: The description of this Job.
        :type description: str
        """

        self._description = description

    @property
    def workplace_type(self) -> str:
        """Gets the workplace_type of this Job.


        :return: The workplace_type of this Job.
        :rtype: str
        """
        return self._workplace_type

    @workplace_type.setter
    def workplace_type(self, workplace_type: str):
        """Sets the workplace_type of this Job.


        :param workplace_type: The workplace_type of this Job.
        :type workplace_type: str
        """
        allowed_values = ["Remote", "Hybird", "On-site"]  # noqa: E501
        if workplace_type not in allowed_values:
            raise ValueError(
                "Invalid value for `workplace_type` ({0}), must be one of {1}"
                .format(workplace_type, allowed_values)
            )

        self._workplace_type = workplace_type

    @property
    def employment_type(self) -> str:
        """Gets the employment_type of this Job.


        :return: The employment_type of this Job.
        :rtype: str
        """
        return self._employment_type

    @employment_type.setter
    def employment_type(self, employment_type: str):
        """Sets the employment_type of this Job.


        :param employment_type: The employment_type of this Job.
        :type employment_type: str
        """

        self._employment_type = employment_type

    @property
    def salary(self) -> str:
        """Gets the salary of this Job.


        :return: The salary of this Job.
        :rtype: str
        """
        return self._salary

    @salary.setter
    def salary(self, salary: str):
        """Sets the salary of this Job.


        :param salary: The salary of this Job.
        :type salary: str
        """

        self._salary = salary

    @property
    def skills(self) -> List[Skill]:
        """Gets the skills of this Job.


        :return: The skills of this Job.
        :rtype: List[Skill]
        """
        return self._skills

    @skills.setter
    def skills(self, skills: List[Skill]):
        """Sets the skills of this Job.


        :param skills: The skills of this Job.
        :type skills: List[Skill]
        """

        self._skills = skills
