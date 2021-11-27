from flask import Flask
from dotenv import load_dotenv

from app.routes import user, candidate, company, job, company, application, skill

load_dotenv()

app = Flask(__name__)


app.register_blueprint(user.user_routes, url_prefix='/user')
app.register_blueprint(candidate.candidate_routes, url_prefix='/candidate')
app.register_blueprint(job.job_routes, url_prefix='/job')
app.register_blueprint(company.company_routes, url_prefix='/company')
app.register_blueprint(application.application_routes,
                       url_prefix='/application')
app.register_blueprint(skill.skill_routes, url_prefix='/skill')


@app.route("/")
def hello():
    return "yo"


@app.route("/users", methods=["GET"])
def get_users():
    users = {
        "users": [{"name": "John", "age": 30}],
    }

    return users
