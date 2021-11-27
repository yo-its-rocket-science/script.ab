import connexion
import six

from swagger_server.models.candidate import Candidate  # noqa: E501
from swagger_server import util


def delete_candidate(id):  # noqa: E501
    """Delete user

    This can only be done by the logged in user. # noqa: E501

    :param id: id of candidate
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def get_candidate_by_id(id):  # noqa: E501
    """get candidate by their id

     # noqa: E501

    :param id: id of candidate.
    :type id: int

    :rtype: Candidate
    """
    return 'do some magic!'


def update_candidate(body, id):  # noqa: E501
    """Updated candidate

    This can only be done by the logged in user. # noqa: E501

    :param body: Updated user object
    :type body: dict | bytes
    :param id: id of candidate.
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Candidate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
