# coding=utf-8
from flask import Blueprint, render_template, abort, request, Response
from bot import send_alert_message

sentry = Blueprint('sentry', __name__)


@sentry.route('/alert', methods=['POST'])
def alert():
    data = request.data
    url = data.get('url')
    message = data.get('')
    level = data.get('level')
    data = {'level': level, 'url': url, 'message': message}
    message = u"Уровень - {level} \n {message} \n {url}".format(**data)
    send_alert_message(message)
    return Response()

