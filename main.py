from flask import Flask, Response, request, make_response
from datetime import datetime
import json
from course import courses
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.route("/test", methods=["GET", "POST"])
def test_flask():
    params = request.args
    body = request.json
    if request.method == "POST":
        msg = {1: "test POST"}
        rsp = Response(json.dumps(msg), status=404, content_type="application/json")
    else:
        msg = {2: "test GET"}
        rsp = make_response(msg)
        rsp.status = 404
        rsp.headers['customHeader'] = 'This is a custom header'

    return rsp


@app.put("/courses/<call_number>")
def put_student(call_number):
    params = request.args
    courses.update_by_key(call_number, params)
    return get_student_by_uni(call_number)


@app.post("/courses")
def post_student():
    body = request.json
    try:
        courses.insert_by_key(body)
    except:
        return Response("Insert Failure", status=404, content_type="text/plain")
    return get_student_by_uni(body["call_number"])


@app.delete("/courses/<call_number>")
def delete_student(call_number):
    try:
        courses.delete_by_key(call_number)
        response = make_response("Delete Success!", 200)
    except:
        response = make_response("Delete Fail!", 400)
    return response


@app.get("/courses")
def get_students_by_template():
    pass


@app.route("/courses/<call_number>", methods=["GET"])
def get_student_by_uni(call_number):
    result = courses.get_by_key(call_number)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)