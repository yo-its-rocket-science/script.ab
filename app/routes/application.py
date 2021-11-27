from flask import Blueprint
from app.controllers import application_controller

application_routes = Blueprint("application_routes", __name__)
