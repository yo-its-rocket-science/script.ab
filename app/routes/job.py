from flask import Blueprint
from app.controllers import job_controller

job_routes = Blueprint('job_routes', __name__)
