from flask import Blueprint
from app.controllers import user_controller

user_routes = Blueprint("user_routes", __name__)

# TODO - Add routes for user_controller
# user_routes.add_url_rule("/", methods=["POST"])(user_controller.create_user)
