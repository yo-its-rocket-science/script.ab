from flask.blueprints import Blueprint

from app.models.skill import Skill  # noqa: E501
from app import util

routes = Blueprint("skill_routes", __name__)


@routes.route("/", methods=["GET"])
def skill_get():  # noqa: E501
    """get list of skills for company to select

     # noqa: E501


    :rtype: List[Skill]
    """
    return 'do some magic!'
