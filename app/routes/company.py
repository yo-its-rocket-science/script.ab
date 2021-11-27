from flask import Blueprint
from app.controllers import company_controller

company_routes = Blueprint("company_routes", __name__)
