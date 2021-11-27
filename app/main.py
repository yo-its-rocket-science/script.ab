from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# TODO: specify routes


@app.route("/")
def hello():
    return "yo"


@app.route("/users", methods=["GET"])
def get_users():
    users = {
        "users": [{"name": "John", "age": 30}],
    }

    return users
