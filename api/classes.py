from flask.views import MethodView
from flask import jsonify, request
from services.classes_service import add_classes_service, add_classesstudent_service, get_classes_service, get_classesstudentsbyid_service, delete_classesstudentbyid_service

class ClassesAPI(MethodView):

    def get(self, class_id):
        """
        Get students in a class
        ---
        tags:
          - classes
        parameters:
          - name: class_id
            in: path
            description: ID of class
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
        return get_classesstudentsbyid_service(class_id)
        
    def delete(self, class_id, student_id):
        """
        Delete a student from class
        ---
        tags:
          - classes
        parameters:
          - name: class_id
            in: path
            description: id of class
            required: true
            type: string
          - name: student_id
            in: path
            description: id of student
            required: true
            type: string
        responses:
          200:
            description: Student deleted from class
        """
        return delete_classesstudentbyid_service(class_id, student_id)

    def post(self, class_id, student_id):
        """
        Assign a Student to a class
        ---
        tags:
          - classes
        parameters:
          - name: class_id
            in: path
            description: id of class
            required: true
            type: string
          - name: student_id
            in: path
            description: id of student
            required: true
            type: string
        responses:
          201:
            description: Student assigned to Classes
          import: "not_found.yaml"
        """
        return add_classesstudent_service(class_id, student_id)

class ClassesItemAPI(MethodView):

    def get(self):
        """
        Get classes
        ---
        tags:
          - classes
        responses:
          200:
            description: Returns a list of classes
            schema:
                type: array
                items:
                    $ref: '#/definitions/Classes'
        """
        return get_classes_service()

    def post(self):
        """
        Create a new class
        ---
        tags:
          - classes
        parameters:
          - in: body
            name: body
            schema:
              id: Classes
              required:
                - class_id
                - name
                - nrOfStudents
              properties:
                class_id:
                  type: string
                  description: id of student class
                name:
                  type: string
                  description: name of class
                nrOfStudents:
                  type: string
                  description: number of students in class
        responses:
          201:
            description: New class created
          import: "not_found.yaml"
        """
        data = request.get_json()
        return add_classes_service(data)
