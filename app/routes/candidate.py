from flask import Blueprint
from app.controllers import candidate_controller

candidate_routes = Blueprint("user_routes", __name__)
