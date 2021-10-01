import redis
from flask import Flask, request

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


@app.route('/', ['GET'])
def hello():
    resp = response()
    return ' {} .\n'.format(resp)


@app.route('/<string:name>/')
def get_student(name):
    return str(r.mget(name)[0], "utf-8")


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name", "")
    grade = request.form.get("grade", "")
    r.mset({name, grade})
    response = "Student {}! with {} grade. added".format(name, grade)
    return response
