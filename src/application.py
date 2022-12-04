from flask import Flask, Response, request, make_response
from datetime import datetime
import json
from course import Courses
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.put("/sections/<call_number>")
def put_section(call_number):
    body = request.form
    Sections.update_by_key(call_number, body)
    return get_section_by_key(call_number)


@app.post("/sections")
def post_section():
    body = request.form
    print(body)
    try:
        Sections.insert_by_key(body)
    except:
        return Response("Insert Failure", status=404, content_type="text/plain")
    return get_section_by_key(body["call_number"])


@app.delete("/sections/<call_number>")
def delete_section(call_number):
    try:
        Sections.delete_by_key(call_number)
        response = make_response("Delete Success!", 200)
    except:
        response = make_response("Delete Fail!", 400)
    return response


@app.route("/sections/<call_number>", methods=["GET"])
def get_student_by_uni(call_number):
    result = Sections.get_by_key(call_number)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.put("/projects/<project_id>")
def put_section(project_id):
    body = request.form
    Projects.update_by_key(project_id, body)
    return get_section_by_key(project_id)


@app.post("/projects")
def post_section():
    body = request.form
    print(body)
    try:
        Projects.insert_by_key(body)
    except:
        return Response("Insert Failure", status=404, content_type="text/plain")
    return get_section_by_key(body["project_id"])


@app.delete("/projects/<project_id>")
def delete_section(project_id):
    try:
        Projects.delete_by_key(project_id)
        response = make_response("Delete Success!", 200)
    except:
        response = make_response("Delete Fail!", 400)
    return response


@app.route("/projects/<project_id>", methods=["GET"])
def get_student_by_uni(project_id):
    result = Projects.get_by_key(project_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.put("/enrollments/<keys>")
def put_enrollment(keys):
    body = request.form
    Enrollments.update_by_key(keys, body)
    return get_enrollment_by_key(keys)


@app.post("/enrollments")
def post_enrollment():
    body = request.form
    print(body)
    try:
        Enrollments.insert_by_key(body)
    except:
        return Response("Insert Failure", status=404, content_type="text/plain")
    return get_enrollment_by_key(body["keys"])


@app.delete("/enrollments/<keys>")
def delete_enrollment(keys):
    try:
        Enrollments.delete_by_key(keys)
        response = make_response("Delete Success!", 200)
    except:
        response = make_response("Delete Fail!", 400)
    return response


@app.route("/enrollments/<keys>", methods=["GET"])
def get_student_by_uni(keys):
    result = Enrollments.get_by_key(keys)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

##############################################################################################

