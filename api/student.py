from flask.views import MethodView
from flask import jsonify, request
from services.student_service import add_student_service, get_student_service, get_studentbyid_service, update_student_service, delete_student_service

class StudentAPI(MethodView):

    def get(self, id):
        """
        Get a student
        ---
        tags:
          - students
        parameters:
          - name: id
            in: path
            description: ID of student
            required: true
            type: string
        responses:
          200:
            description: Returns a list of students
            schema:
                type: array
                items:
                    $ref: '#/definitions/Student'
        """
        return get_studentbyid_service(id)
        
    def put(self, id):
        """
        Update a student
        ---
        tags:
          - students
        parameters:
          - name: id
            in: path
            description: ID of student
            required: true
            type: string
          - in: body
            name: body
            schema:
              id: Student
              required:
                - firstname
                - lastname
                - phone
                - email
                - class_id
              properties:
                firstname:
                  type: string
                  description: firstname of student
                lastname:
                  type: string
                  description: lastname of student
                phone:
                  type: string
                  description: phone number of student
                email:
                  type: string
                  description: email address of student
                class_id:
                  type: string
                  description: id of student class
        responses:
          201:
            description: Student updated
            schema:
                type: array
                items:
                    $ref: '#/definitions/Student'
        """
        student_data = request.get_json()
        return update_student_service(id, student_data)

    def delete(self, id):
        """
        Delete a student
        ---
        tags:
          - students
        parameters:
          - name: id
            in: path
            description: id of student
            required: true
            type: string
        responses:
          200:
            description: Student deleted
            schema:
                type: array
                items:
                    $ref: '#/definitions/Student'
        """
        return delete_student_service(id)

class StudentListAPI(MethodView):

    def get(self):
        """
        Get a list of students
        ---
        tags:
          - students
        responses:
          200:
            description: Returns a list of students
            schema:
                type: array
                items:
                    $ref: '#/definitions/Student'
        """
        return get_student_service()

    def post(self):
        """
        Create a new student
        ---
        tags:
          - students
        parameters:
          - in: body
            name: body
            schema:
              id: Student
              required:
                - firstname
                - lastname
                - phone
                - email
                - class_id
              properties:
                firstname:
                  type: string
                  description: firstname of student
                lastname:
                  type: string
                  description: lastname of student
                phone:
                  type: string
                  description: phone number of student
                email:
                  type: string
                  description: email address of student
                class_id:
                  type: string
                  description: id of student class
        responses:
          201:
            description: New student created
            schema:
                type: array
                items:
                    $ref: '#/definitions/Student'
          import: "not_found.yaml"
        """
        data = request.get_json()
        return add_student_service(data)
