# coding=utf-8
import json
from flask import Blueprint, render_template, abort, request, Response
from bot import send_alert_message

sentry = Blueprint('sentry', __name__)


@sentry.route('/alert', methods=['POST'])
def alert():
    data = request.data
    data = json.loads(data)
    url = data.get('url')
    message = data.get('message')
    detail = data.get('culprit')
    level = data.get('level')
    data = {'level': level, 'url': url, 'message': message, 'detail': detail}
    message = u"Ошибка! \n Уровень - {level} \n {message} \n {detail} \n {url}".format(**data)
    send_alert_message(message)
    return Response()

