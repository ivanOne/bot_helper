from flask import Flask
from sentry.controller import sentry

app = Flask(__name__)
app.register_blueprint(sentry)


if __name__ == '__main__':
    app.run()