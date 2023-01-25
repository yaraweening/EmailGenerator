import os
from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger.utils import swag_from
from mongoengine import connect
from api.student import StudentAPI, StudentListAPI
from api.classes import ClassesAPI, ClassesItemAPI

app = Flask(__name__)

app.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "Flasgger",
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
        ('Access-Control-Allow-Credentials', "true"),
    ],
    "specs": [
        {
            "version": "1.0.0",
            "title": "Api v1",
            "endpoint": 'v1_spec',
            "description": 'This is the version 1 of our API',
            "route": '/v1/spec',
            "rule_filter": lambda rule: rule.endpoint.startswith(
                'should_be_v1_only'
            ),
            "definition_filter": lambda definition: (
                'v1_model' in definition.tags)
        }
    ],
    "ui_params":
    {
        "apisSorter": "alpha",
        "operationsSorter": "alpha",
        "tagsSorter": "alpha"
    }   
}

swag = Swagger(app)
connect(db='StudentsMS', alias="StudentsMS", host=os.environ.get('MONGO_URI'))
connect(db='ClassesMS', alias="ClassesMS", host=os.environ.get('MONGO_URI'))

@app.after_request
def allow_origin(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://example.com'
    response.headers['Access-Control-Allow-Credentials'] = 'true'

    return response

view = StudentAPI.as_view('students')
viewList = StudentListAPI.as_view('students')
app.add_url_rule(
    '/v1/students',
    view_func=viewList,
    methods=['GET'],
    endpoint='should_be_v1_only_all'
)
app.add_url_rule(
    '/v1/students/<string:id>',
    view_func=view,
    methods=['GET'],
    endpoint='should_be_v1_only'
)
app.add_url_rule(
    '/v1/students/<string:id>',
    view_func=view,
    methods=['PUT'],
    endpoint='should_be_v1_only_put'
)
app.add_url_rule(
    '/v1/students/<string:id>',
    view_func=view,
    methods=['DELETE'],
    endpoint='should_be_v1_only_delete'
)
app.add_url_rule(
    '/v1/students',
    view_func=viewList,
    methods=['POST'],
    endpoint='should_be_v1_only_post'
)

classesView = ClassesAPI.as_view('classes')
classesViewItem = ClassesItemAPI.as_view('classes')
app.add_url_rule(
    '/v1/classes/<string:class_id>/students',
    view_func=classesView,
    methods=['GET'],
    endpoint='should_be_v1_only_classes'
)
app.add_url_rule(
    '/v1/classes/<string:class_id>/students/<string:student_id>',
    view_func=classesView,
    methods=['POST'],
    endpoint='should_be_v1_only_classes_post_assign'
)
app.add_url_rule(
    '/v1/classes/<string:class_id>/students/<string:student_id>',
    view_func=classesView,
    methods=['DELETE'],
    endpoint='should_be_v1_only_classes_delete'
)
app.add_url_rule(
    '/v1/classes',
    view_func=classesViewItem,
    methods=['POST'],
    endpoint='should_be_v1_only_classes_post'
)

@app.route("/")
def startup():
    return """
      <h1>Order API</h1>
      <p>
        The APIs are served by a swagger UI on
        <a href="/apidocs/index.html">Api docs</a>
      </p>
    """

@app.route("/tos")
def tos():
    return """
      <h1>Order API</h1>
      <p>
        The APIs are served by a swagger UI on
        <a href="/apidocs/index.html">Api docs</a>
      </p>
    """

if __name__ == "__main__":
    app.run(debug=True)