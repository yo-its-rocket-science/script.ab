from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "yo"


@app.route("/users", methods=["GET"])
def get_users():
    users = {
        "users": {"name": "John", "age": 30},
    }

    return users


if __name__ == "__main__":
    app.run(debug=True)
