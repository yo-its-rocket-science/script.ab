import flask
from flask import Blueprint
from flask.globals import request
from app.models.user import User  # noqa: E501


routes = Blueprint("user_routes", __name__)


@routes.route('/', methods=['POST', 'PUT'])
def index():  # noqa: E501
    if request.method == 'POST':

        content = request.json
        """Create user

        This can only be done by the logged in user. # noqa: E501

        :param body: Created user object
        :type body: dict | bytes

        :rtype: None
        """

        return 'create user'
    elif request.method == 'PUT':

        content = request.json
        """Update user
        """
        return 'update user'


@routes.route('/<username>', methods=['GET'])
def get_user_by_name(username):  # noqa: E501
    """Get user by id

     # noqa: E501

    :param username: The name that needs to be fetched. Use user1 for testing. 
    :type username: str

    :rtype: User
    """
    return 'get user'


@routes.route('/login', methods=['POST'])
def login_user(username, password):  # noqa: E501
    """Logs user into the system

     # noqa: E501

    :param username: The user name for login
    :type username: str
    :param password: The password for login in clear text
    :type password: str

    :rtype: str
    """
    return 'do some magic!'


@routes.route('/logout', methods=['POST'])
def logout_user():  # noqa: E501
    """Logs out current logged in user session

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
