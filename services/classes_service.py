from model.student import Student
from model.classes import Classes
from flask import make_response
from utils.DecimalEncoder import Encoder
import json
from utils.JwtToken import validate_token

def add_classes_service(classes_data):
    try:
        class_Id = classes_data['class_id']
        name = classes_data['name']
        nrOfStudents = classes_data['nrOfStudents']

        classes = Classes(class_id=class_Id, name=name, nrOfStudents=nrOfStudents)
        classes.save()
        return make_response({'message' : f'succesfully inserted classes with id: {classes.class_id}'}, 201)
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  

def add_classesstudent_service(class_id, student_id):
    try:
        student = Student.objects(id=student_id)
        if student:     
            student = student.get(id=student_id)
            student.class_id = class_id
            student.save()
            
            classes = Classes.objects(class_id=class_id)
            if classes:
                classes = classes.get(class_id=class_id)
                classes.nrOfStudents = classes.nrOfStudents + 1
                classes.save()

        return make_response({'message' : f'succesfully inserted classes for student'}, 201)
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  

def get_classesstudentsbyid_service(class_id):
    students = []
    try:
        student_data = Student.objects(class_id=class_id)
        for student in student_data:
            student_data = {}
            student_data['_id'] = str(student.id)
            student_data['firstname'] = student.firstname
            student_data['lastname'] = student.lastname
            student_data['phone'] = student.phone
            student_data['email'] = student.email
            student_data['class_id'] = student.class_id
            students.append(student_data)

        return {"student": students}
    except Exception as e:
        return make_response({'message' : str(e)}, 404)  

def delete_classesstudentbyid_service(class_id, student_id):
    try:
        student = Student.objects(id=student_id)
        if student:     
            student = student.get(id=student_id)
            student.class_id = 0
            student.save()
            
            classes = Classes.objects(class_id=class_id)
            if classes:
                classes = classes.get(class_id=class_id)
                classes.nrOfStudents = classes.nrOfStudents - 1
                classes.save()
        
            return make_response({'message' : 'succesfully deleted'}, 200)
        else:
            return make_response({'message' : 'class does not exists'}, 404)   
    except Exception as e:
        return make_response({'message' : str(e)}, 404)   
        