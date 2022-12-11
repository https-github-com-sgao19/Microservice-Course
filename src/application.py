from flask import Flask, Response, request, make_response
from datetime import datetime
import json
from flask_cors import CORS
from Sections import Sections
from Projects import Projects
from Enrollments import Enrollments

# Create the Flask application object.
application = Flask(__name__)

CORS(application)


@application.put("/sections/<call_number>")
def put_section(call_number):
    body = request.json
    Sections.update_by_key(call_number, body)
    return Sections.get_by_key(call_number)

@application.post("/sections")
def post_section():
    body = request.json
    try:
        Sections.insert_by_key(body)
    except:
        return Response("Insert Failure", status=404, content_type="text/plain")
    return Sections.get_by_key(body["call_number"])

#
@application.delete("/sections/<call_number>")
def delete_section(call_number):
    try:
        Sections.delete_by_key(call_number)
        response = make_response("Delete Success!", 200)
    except:
        response = make_response("Delete Fail!", 400)
    return response


@application.get("/sections/<call_number>")
def get_sections(call_number):
    result = Sections.get_by_key(call_number)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.put("/projects/<project_id>")
def put_project(project_id):
    body = request.json
    Projects.update_by_key(project_id, body)
    return Projects.get_by_key(project_id)


@application.post("/projects")
def post_project():
    body = request.json
    try:
        Projects.insert_by_key(body)
    except:
        return Response("Insert Failure", status=404, content_type="text/plain")
    return Projects.get_by_key(body["project_id"])

#

#
@application.route("/projects/<project_id>", methods=["GET"])
def get_project(project_id):
    result = Projects.get_by_key(project_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.get("/projects")
def get_project_by_params():
    params = request.args
    result = Projects.get_by_params(params)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.delete("/projects/<keys>")
def delete_projects(keys):
    try:
        Projects.delete_by_key(keys)
        response = make_response("Delete Success!", 200)
    except:
        response = make_response("Delete Fail!", 400)
    return response


@application.put("/enrollments")
def put_enrollment():
    params = request.args
    body = request.json
    Enrollments.update_by_key(params, body)
    return Enrollments.get_by_key(params)



@application.post("/enrollments")
def post_enrollment():
    body = request.json
    try:
        Enrollments.insert_by_key(body)
    except:
        return Response("Insert Failure", status=404, content_type="text/plain")
    return Enrollments.get_by_key(body)


@application.delete("/enrollments/<keys>")
def delete_enrollment(keys):
    keys = keys.split(",")
    try:
        Enrollments.delete_by_key(keys)
        response = make_response("Delete Success!", 200)
    except:
        response = make_response("Delete Fail!", 400)
    return response


@application.route("/enrollments/<keys>", methods=["GET"])
def get_enrollments(keys):
    result = Enrollments.get_by_key(keys)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

####################分页
@application.get("/sections")
def get_sections_by_template():
    params = request.args
    sections_per_page = int(params["limit"]) if "limit" in params else 10
    offset = sections_per_page * (int(params["page"]) - 1) if "page" in params else 0

    result = Sections.get_by_template(10, offset)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.get("/project/<call_no>")
def get_project_by_call_no(call_no):
    result = Projects.get_by_course(call_no)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.get('/<uni>')
def get_uni(uni):
    result = Enrollments.join_s(uni)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")
    return rsp

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5011)

##############################################################################################

