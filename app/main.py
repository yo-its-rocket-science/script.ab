from flask import Flask
from dotenv import load_dotenv

from app.controllers import user_controller, candidate_controller, company_controller, job_controller, application_controller, skill_controller

load_dotenv()

app = Flask(__name__)


app.register_blueprint(user_controller.routes, url_prefix='/user')
app.register_blueprint(candidate_controller.routes, url_prefix='/candidate')
app.register_blueprint(job_controller.routes, url_prefix='/job')
app.register_blueprint(company_controller.routes, url_prefix='/company')
app.register_blueprint(application_controller.routes,
                       url_prefix='/application')
app.register_blueprint(skill_controller.routes, url_prefix='/skill')
