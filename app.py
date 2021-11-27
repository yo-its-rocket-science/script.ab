from flask import Flask

app = Flask("script.ab")


@app.route("/")
def hello():
    return "yo"


if __name__ == "__main__":
    app.run()
