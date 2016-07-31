from flask import Blueprint, render_template, abort, request, Response
from bot import send_alert_message

sentry = Blueprint('sentry', __name__)


@sentry.route('/alert')
def alert():
    send_alert_message()
    return Response()

