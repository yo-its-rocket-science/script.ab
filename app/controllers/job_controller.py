import connexion
import six

from swagger_server.models.job import Job  # noqa: E501
from swagger_server import util


def delete_job(id):  # noqa: E501
    """Delete job

    This can only be done by the logged in job. # noqa: E501

    :param id: The job that needs to be deleted
    :type id: float

    :rtype: None
    """
    return 'do some magic!'


def get_job_by_id(id):  # noqa: E501
    """get job by id

     # noqa: E501

    :param id: id of job.
    :type id: int

    :rtype: Job
    """
    return 'do some magic!'


def job_post():  # noqa: E501
    """add job

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def putjob(body, id):  # noqa: E501
    """putjob

     # noqa: E501

    :param body: Updated job object
    :type body: dict | bytes
    :param id: id of job.
    :type id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Job.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
