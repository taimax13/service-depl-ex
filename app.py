import json
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)


def response():
    stList = r.keys()
    output = ''
    output += '<html><body>'
    output += '<h1>Students list</h1>'
    for st in stList:
        output += str(st, "utf-8")
        output += " : "
        output += str(r.mget(st)[0], "utf-8")
        output += '</br>'
    output += '</body></html>'
    return output.encode()


class AddData:
    def post(self, jsonF):
        with open(jsonF) as file:
            jObj = json.load(file)
            file.close()
        redis.Redis().mset(jObj)


@app.route('/')
def hello():
    resp = response()
    return ' {} .\n'.format(resp)
