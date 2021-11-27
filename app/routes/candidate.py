from flask import Blueprint
from app.controllers import candidate_controller

candidate_routes = Blueprint("candidate_routes", __name__)
