import datetime

from flask import Flask, Response, request, logging
from sentry.controller import sentry

app = Flask(__name__)
app.register_blueprint(sentry)


@app.before_request
def pre_request_logging():
    dt = datetime.datetime.today().ctime()
    addr = request.remote_addr
    method = request.method
    url = request.url
    data = request.data
    headers = ', \n'.join([': '.join(x) for x in request.headers])
    kw = {'dt': dt, 'addr': addr, 'method': method, 'url': url, 'data': data, 'headers': headers}
    str_log = "{dt} \n {addr} \n {method} \n {url} \n {data} \n headers: \n {headers}\n -------------------\n"\
        .format(**kw)
    with open("test.txt", "a") as myfile:
        myfile.write(str_log)


@app.route("/")
def default_response():
    return Response("OK")


if __name__ == '__main__':
    app.run()
