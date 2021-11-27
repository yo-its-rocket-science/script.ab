from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app import util


class User(Model):
    def __init__(self, id: int = None, username: str = None, password: str = None, first_name: str = None, last_name: str = None, phone: str = None, image: str = None, user_status: int = None, candidate_id: int = None, company_id: int = None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: int
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param password: The password of this User.  # noqa: E501
        :type password: str
        :param first_name: The first_name of this User.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this User.  # noqa: E501
        :type last_name: str
        :param phone: The phone of this User.  # noqa: E501
        :type phone: str
        :param image: The image of this User.  # noqa: E501
        :type image: str
        :param user_status: The user_status of this User.  # noqa: E501
        :type user_status: int
        :param candidate_id: The candidate_id of this User.  # noqa: E501
        :type candidate_id: int
        :param company_id: The company_id of this User.  # noqa: E501
        :type company_id: int
        """
        self.swagger_types = {
            'id': int,
            'username': str,
            'password': str,
            'first_name': str,
            'last_name': str,
            'phone': str,
            'image': str,
            'user_status': int,
            'candidate_id': int,
            'company_id': int
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'password': 'password',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'phone': 'phone',
            'image': 'image',
            'user_status': 'userStatus',
            'candidate_id': 'candidateId',
            'company_id': 'companyId'
        }
        self._id = id
        self._username = username
        self._password = password
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._image = image
        self._user_status = user_status
        self._candidate_id = candidate_id
        self._company_id = company_id

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: int
        """

        self._id = id

    @property
    def username(self) -> str:
        """Gets the username of this User.


        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this User.


        :param username: The username of this User.
        :type username: str
        """

        self._username = username

    @property
    def password(self) -> str:
        """Gets the password of this User.


        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this User.


        :param password: The password of this User.
        :type password: str
        """

        self._password = password

    @property
    def first_name(self) -> str:
        """Gets the first_name of this User.


        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this User.


        :param first_name: The first_name of this User.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this User.


        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this User.


        :param last_name: The last_name of this User.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def phone(self) -> str:
        """Gets the phone of this User.


        :return: The phone of this User.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this User.


        :param phone: The phone of this User.
        :type phone: str
        """

        self._phone = phone

    @property
    def image(self) -> str:
        """Gets the image of this User.


        :return: The image of this User.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this User.


        :param image: The image of this User.
        :type image: str
        """

        self._image = image

    @property
    def user_status(self) -> int:
        """Gets the user_status of this User.

        User Status  # noqa: E501

        :return: The user_status of this User.
        :rtype: int
        """
        return self._user_status

    @user_status.setter
    def user_status(self, user_status: int):
        """Sets the user_status of this User.

        User Status  # noqa: E501

        :param user_status: The user_status of this User.
        :type user_status: int
        """

        self._user_status = user_status

    @property
    def candidate_id(self) -> int:
        """Gets the candidate_id of this User.


        :return: The candidate_id of this User.
        :rtype: int
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id: int):
        """Sets the candidate_id of this User.


        :param candidate_id: The candidate_id of this User.
        :type candidate_id: int
        """

        self._candidate_id = candidate_id

    @property
    def company_id(self) -> int:
        """Gets the company_id of this User.


        :return: The company_id of this User.
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id: int):
        """Sets the company_id of this User.


        :param company_id: The company_id of this User.
        :type company_id: int
        """

        self._company_id = company_id
