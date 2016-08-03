from flask import Flask, Response
from sentry.controller import sentry

app = Flask(__name__)
app.register_blueprint(sentry)


@app.route("/")
def default_response():
    return Response("OK")


if __name__ == '__main__':
    app.run()