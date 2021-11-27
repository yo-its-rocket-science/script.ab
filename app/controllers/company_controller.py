import flask
import six

from app.models.company import Company  # noqa: E501
from app import util


def add_company(body):  # noqa: E501
    """add company

     # noqa: E501

    :param body: Updated user object
    :type body: dict | bytes

    :rtype: None
    """
    if flask.request.is_json:
        body = Company.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_company(id):  # noqa: E501
    """delete_company

     # noqa: E501

    :param id: id of Company.
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_company_by_id(id):  # noqa: E501
    """Get candidate by id

     # noqa: E501

    :param id: The id that needs to be fetched.
    :type id: float

    :rtype: Company
    """
    return 'do some magic!'


def put_company(body, id):  # noqa: E501
    """put_company

     # noqa: E501

    :param body: Updated Company object
    :type body: dict | bytes
    :param id: id of Company.
    :type id: int

    :rtype: None
    """
    if flask.request.is_json:
        body = Company.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'
