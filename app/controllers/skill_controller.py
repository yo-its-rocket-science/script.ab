from flask.blueprints import Blueprint
from flask import jsonify

from app.models.skill import Skill  # noqa: E501

routes = Blueprint("skill_routes", __name__)


@routes.route("/", methods=["GET"])
def skill_get():  # noqa: E501
    """get list of skills for company to select

     # noqa: E501


    :rtype: List[Skill]
    """

    skills = [
        Skill(id=1, name="Java").to_dict(),
        Skill(id=2, name="Python").to_dict(),
        Skill(id=3, name="C++").to_dict(),
        Skill(id=4, name="C#").to_dict(),
        Skill(id=5, name="JavaScript").to_dict(),
        Skill(id=6, name="PHP").to_dict(),
        Skill(id=7, name="Ruby").to_dict(),
        Skill(id=8, name="Swift").to_dict(),
        Skill(id=9, name="Objective-C").to_dict(),
        Skill(id=10, name="Go").to_dict(),
        Skill(id=11, name="C").to_dict(),
        Skill(id=12, name="CoffeeScript").to_dict(),
        Skill(id=13, name="Perl").to_dict(),
    ]

    return jsonify(skills)
